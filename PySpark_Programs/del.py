import sys

from pyspark.sql import *
#from lib.logger import Log4j


if __name__ == "__main__":
    spark = SparkSession.builder.appName('delete_later').master('local[2]').getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel("ERROR")
    df = spark.read.format('csv').option('header',True).option('inferSchema',True).load('Data/survey.csv')
#    logger = Log4j(spark)
    df.createTempView('survey')
    df2 = spark.sql('select * from survey limit 10')
    df2.show(10)