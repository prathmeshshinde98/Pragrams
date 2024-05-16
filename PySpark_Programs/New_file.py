from pyspark.sql import *

if __name__ == '__main__':
    spark = SparkSession.builder.appName("trial").master("local[2]").getOrCreate()
    df = spark.read.format("CSV").option("header",True).option("inferSchema",True).load("Data/Movies_CGPT.csv")
    #df.show()

    spark.catalog.dropTempView("Movies")
    df.createTempView("Movies")
    df2 = spark.sql("select * from Movies where movieID= 2")
    df = df.union(df2)
    df.show()
    df.printSchema()