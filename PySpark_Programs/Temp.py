from pyspark.sql.functions import lit

def filter_func(spark,file_read):
    df = file_read.filter("Age > 40").select("Age", "Gender", "Country")
    return df.withColumn("Temp_column",lit("Temp Value"))