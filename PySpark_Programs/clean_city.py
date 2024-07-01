from pyspark.sql import *
from pyspark.sql.functions import col
if __name__ == "__main__":
    spark = SparkSession.builder.master('local[1]').appName('clean_city').getOrCreate()
    df = spark.read.format('csv').option('header',True).load('Data/clean_city_india.csv')

    sangli_df = df.filter('district = "Sangli"')
    sangli_df.show()

    sindhudurg_df = df.filter('district = "Sindhudurg"')
    #sindhudurg_df.show()

    kolhapur_df = df.filter('district = "Kolhapur"')
    #kolhapur_df.show()

    overall_cleanliest_cities = df.filter('State = "Maharashtra"').orderBy(col('2023_Score_Max10000').desc(),col('2022_Score_Max7500').desc(),col('2020_Score_Max6000').desc(),col('2019_Score_5000').desc(),col('2018_Score').desc(),col('2017_Score').desc(),col('2016_Score').desc())
    overall_cleanliest_cities.show(20)

    t23_cleanliest_cities = df.filter('State = "Maharashtra"').orderBy(col('2023_Score_Max10000').desc())
    t23_cleanliest_cities.show(20)

    t22_cleanliest_cities = df.filter('State = "Maharashtra"').orderBy(col('2022_Score_Max7500').desc())
    t22_cleanliest_cities.show(20)