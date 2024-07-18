from pyspark.sql import *
from pyspark.sql.functions import col, like
import pandas as pd

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[2]").appName("Crypto").getOrCreate()
    df = spark.read.format('csv').option('Header',True).option('inferSchema',True).load('Data/Crypto.csv')
    df.show(truncate = False)
    print(df.head(5))
    print(df.tail(5))
    #pd.set_option('display.max_columns',10)
    #schema_df = pd.read_csv('Data/Crypto.csv')
    #print(schema_df)

