from pyspark.sql import *
from pyspark.sql.functions import col, when, lit, sum, min, max

if __name__ == "__main__":
    spark = SparkSession.builder.master('local[1]').appName("orders_chatgpt").getOrCreate()
    df = spark.read.format('csv').option('header',True).load('Data/orders.csv')

    df1 = df.select(col('OrderID').cast('Int'),col('CustomerId').cast('Int'),\
                    col('OrderDate').cast('Date'),col('ProductID').cast('Int'),\
                    col('Quantity').cast('Int'),col('Price').cast('Float'))

    df2 = df1.withColumn('TotalPrice', df1.Quantity*df1.Price)

    #Calculate the total sales ("TotalPrice") for each product
    df3 = df2.groupBy('ProductID').agg(sum('TotalPrice')).orderBy("ProductID")
    df3.show()

    #Calculate the number of unique customers
    df4 = df2.select('CustomerID').distinct()

    print('Total number of uniquer customers are - ' + str(df4.count()))
    print('Customers as below')
    df4.show()

    #Find the customer who spent the most
    df5 = df2.groupBy('CustomerID').agg(sum('TotalPrice').alias('TotalPrice'))\
        .orderBy(col('TotalPrice').desc()).first()
    print(df5)


