import pyspark
from pyspark.sql import *
from pyspark.sql.functions import when, col, lit, concat_ws, min, split

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Data Clean").master("local[2]").getOrCreate()

    df = spark.read.format("csv").option("header", "true").option("multiline", "true").load("Data/Data_clean.csv")
    df.show()

    df1 = df.select(col("id").alias("id"),
                    when(df.ind == lit("FN"), df.fname).otherwise("null").alias("fname"),
                    when(df.ind == lit("LN"), df.fname).otherwise("null").alias("lname"),
                    when(df.ind == lit("AD"), concat_ws(", ",df.fname,df.lname,df.apartment,df.street)).otherwise("null").alias("address"),
                    when(df.ind == lit("PH"), df.fname).otherwise("null").alias("phone")
                    )
    df1.show()

    df2 = df1.groupby("id").agg(min(df1.fname).alias("fname"),
                                min(df1.lname).alias("lname"),
                                min(df1.address).alias("address"),
                                min(df1.phone).alias("phone"))
    
    df2.show()

    df3 = df2.withColumn("apartment", split(df2.address, ',').getItem(0)) \
            .withColumn("street", split(df2.address, ',').getItem(1)) \
            .withColumn("city", split(df2.address, ',').getItem(2))\
            .withColumn("country", split(df2.address, ',').getItem(3))

    df3 = df3.select("id","fname","lname","apartment","street","city","country","phone")
    df3.show()

    spark.stop()
    # df3.write.option("header",True).csv("Data/Data_cleaned")
    # df3.toPandas().to_csv("Data/Data_cleaned.csv")