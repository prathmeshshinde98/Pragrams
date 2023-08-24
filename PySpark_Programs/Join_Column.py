from pyspark.sql import *
from pyspark.sql.functions import when, lit, col
import pandas as pd
if __name__ == "__main__":
    spark = SparkSession.builder.appName("test").master("local[2]").getOrCreate()

    student_data1 = [(36, "Parth", "Vita","BTech"),
                    (33, "Pihu", "Oros", "MPharm"),
                    (69, "Chotu", "Unknown", "Unknown")]

    student_data2 = [(10, "Mr.Mini", "Lala", "MBA", "6"),
                     (10, "Mrs.Mini", "Lala", "Doctor", "5.10")]

    details1 = ["Age", "Name", "Location", "Education"]
    details2 = ["Age", "Name", "Location", "Education", "Height"]

    df1 = spark.createDataFrame(data= student_data1, schema= details1)
    df2 = spark.createDataFrame(data= student_data2, schema= details2)

    df1 = df1.withColumn("Height", lit("5.10"))
    df = df1.union(df2)
    df3 = df.select(col("Age").alias("Vay"),"Name", "Location", "Education", "Height")
    df3.show()