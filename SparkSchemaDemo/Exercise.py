from pyspark.sql import *
from pyspark.sql.functions import col,lit

if __name__ == '__main__':
    spark = SparkSession.builder.master('local[2]').appName('exercise').getOrCreate()
    df = spark.read.format('csv').option('header',True).option('schemaName',True).load('Data/Sales_CGPT.csv')
    # Select 5 Rows only
    df2 = df.limit(5)
    # Multiplication of Quantity and PricePerUnit to get TotalSales numbers
    df3 = df.withColumn("TotalSales", col("Quantity") * col("PricePerUnit"))
    # Total Sales for a Individual Product
    df4 = df3.groupBy("Product").sum("TotalSales")
    # Typecast Quantity column to integer to add all the quantity for individual product
    df5 = df3.withColumn("Quantity", col("Quantity").cast("integer"))
    # Adding the Quantity
    df5.show()
    df6 = df5.groupBy("Product").sum("Quantity")
    # Adding Sum of Quantity Dataframe(df6) to Sum of TotalSales Dataframe(df4)
    df7 = df6.join(df4.select("Product","sum(TotalSales)"),on="Product",how="inner")
    # Rename columns to proper naming
    df8 = df7.withColumnRenamed("sum(Quantity)","Quantity").withColumnRenamed("sum(TotalSales)","TotalRevenue")
    df9 = df8.sort("Quantity")
    df8.show()
    df9.show()
    spark.stop()