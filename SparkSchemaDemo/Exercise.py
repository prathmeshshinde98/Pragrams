from pyspark.sql import *

if __name__ == '__main__':
    spark = SparkSession.builder.master('local[2]').appName('exercise').getOrCreate()
    df = spark.read.format('csv').option('header',True).option('schemaName',True).load('Data/ChatGPT.csv')
    df.show()
    spark.stop()