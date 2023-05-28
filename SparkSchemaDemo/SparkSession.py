from pyspark.sql import *
from pyspark.sql.functions import col
from Temp import *
if __name__ == '__main__':
    spark = SparkSession.builder.master("local[2]").appName("try").getOrCreate()

    file_read = spark.read.format("csv")\
        .option("header", True)\
        .option("inferSchema", True)\
        .load("Data/survey.csv")
    filter_read = filter_func(spark, file_read)
    filter_read.show()
