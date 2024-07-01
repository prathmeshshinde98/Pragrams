from pyspark.sql import *
from pyspark.sql.functions import col

if __name__ == "__main__":
    spark = SparkSession.builder.master("local[2]").appName("Crypto").getOrCreate()
    df = spark.read.format('csv').option('Header',True).option('inferSchema',True).load('Data/Crypto.csv')
    df.show(5) #21347

    #print(df.count())
    # abbr # BTC ETH