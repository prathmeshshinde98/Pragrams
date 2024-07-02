from pyspark.sql import *
from pyspark.sql.functions import col, when, min
from timeit import default_timer as timer


def show_crypto_data(spark_crypto_cln):
    df = spark_crypto_cln.read.format('CSV').option('Header', True).option('SchemaReader', True).load('Data/Crypto.csv')
    # See all rows data without sub stringing the column data
    df.show(truncate=False)

    # See the detailed row and column [x][y]. Pinpoint the cell.
    row = df.collect()[0]
    column = df.collect()[0][2]
    print(row)
    print(column)


def data_clean(spark_data_clean):
    start = timer()
    df = spark_data_clean.read.format('CSV').option('Header', True).load('Data/Data_clean.csv')
    df1 = df.select(col('id').alias('id'),
                    when(df.ind == 'FN', col('fname')).otherwise('null').alias('fname'),
                    when(df.ind == 'LN', col('fname')).otherwise('null').alias('lname'),
                    when(df.ind == 'AD', col('fname')).otherwise('null').alias('apartment'),
                    when(df.ind == 'AD', col('lname')).otherwise('null').alias('street'),
                    when(df.ind == 'AD', col('apartment')).otherwise('null').alias('city'),
                    when(df.ind == 'AD', col('street')).otherwise('null').alias('country'),
                    when(df.ind == 'PH', col('fname')).otherwise('null').alias('phone'))
    # df.show()
    # df1.show(truncate=False)

    df2 = df1.groupby('id').agg(min(df1.fname).alias('fname'),
                                min(df1.lname).alias('lname'),
                                min(df1.apartment).alias('apartment'),
                                min(df1.street).alias('street'),
                                min(df1.city).alias('city'),
                                min(df1.country).alias('country'),
                                min(df1.phone).alias('phone'))
    df2.show()
    stop = timer()
    print(stop-start)


if __name__ == '__main__':
    spark = SparkSession.builder.appName('FirstJuly2024').master('local[2]').getOrCreate()
    # show_crypto_data(spark)
    data_clean(spark)