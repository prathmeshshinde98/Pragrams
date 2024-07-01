from pyspark.sql import *

if __name__ == '__main__':
    spark = SparkSession.builder.appName('FirstJuly2024').master('local[2]').getOrCreate()
    df = spark.read.format('CSV').option('Header', True).option('SchemaReader', True).load('Data/Crypto.csv')
    df.show(truncate=False)

    row = df.collect()[0]
    column = df.collect()[0][2]
    print(row)
    print(column)