from pyspark.sql import *
from pyspark.sql.functions import col

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[3]").appName("Movies_rating_exercise").getOrCreate()
    file1 = spark.read.format("CSV").option("header",True).load("Data/Movies_CGPT.csv")
    file2 = spark.read.format("CSV").option('header',True).load("Data/Movies_ratings_CGPT.csv")
    df2 = file2.withColumn("rating", col("rating").cast("double"))
    df3 = df2.groupby('movieId').avg('rating')
    # df4 = df2.join(df3.select("userId","movieId","timestamp"),on = "movieId",how ="inner")
    # df2.show()
    df4.show()
    spark.stop()