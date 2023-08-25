from pyspark.sql import *
from pyspark.sql.functions import col

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[3]").appName("Movies_rating_exercise").getOrCreate()
    file1 = spark.read.format("CSV").option("header",True).load("Data/Movies_CGPT.csv")
    file2 = spark.read.format("CSV").option('header',True).load("Data/Movies_ratings_CGPT.csv")
    df2 = file2.withColumn("rating", col("rating").cast("double"))
    df3 = df2.groupby('movieId').avg('rating')
    df2.show()
    file1.show()
    file2.show()
    spark.stop()