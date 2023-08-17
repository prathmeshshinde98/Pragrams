from pyspark.sql import *
from pyspark.sql.functions import col, count, when, isnull
if __name__ == "__main__":
    spark = SparkSession.builder.appName("Cleaning Operations").master("local[2]").getOrCreate()

    df = spark.read.format("csv").option("Header","True").csv("Data/Admission_Prediction.csv")
    df_1 = df.select(*(col(c).cast("float").alias(c) for c in df.columns))

    df_2 = df_1.select([count(when(col(c).isNull(), c)).alias(c) for c in df_1.columns])

    df_2.show()
    # df_1.show()
    # df_1.printSchema()