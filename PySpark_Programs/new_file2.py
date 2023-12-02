from pyspark.sql import *
from pyspark.sql.functions import desc
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,DateType

if __name__ == "__main__":
    spark = SparkSession.builder.appName("SQL Tables").master("local[2]").getOrCreate()
    df = spark.read.format("csv").option("Header",True).option("Inferschema",True).load("Data/Fire_Department_Calls_for_Service.csv")
    df.show(10)
    df1 = df.groupBy("Call Type","Call Final Disposition").count().orderBy(desc("count"))
    # df1.createTempView("Fire_Calls")
    df1.show()
    spark.stop()