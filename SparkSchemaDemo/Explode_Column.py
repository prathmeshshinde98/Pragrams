from pyspark.sql import *
from pyspark.sql.functions import explode

if __name__ == "__main__":

    spark = SparkSession.builder.appName("Column_Explode").master("local[2]").getOrCreate()

    data = [(1,["Prathmesh","Shinde", "CS Engineer"]),
            (2,["Preetam","Palkar", "Pharmacist"])]
    details = ["ID","Name"]

    df = spark.createDataFrame(data=data, schema=details)
    df = df.select(df.ID, explode(df.Name).alias("Name"))
    df.printSchema()
    df.show()