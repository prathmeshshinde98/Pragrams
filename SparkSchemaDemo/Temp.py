

def filter_func(spark,file_read):
    return file_read.filter("Age > 40").select("Age", "Gender", "Country")



    details1 = ["Age", "Name", "Place", "Education"]
    details2 = ["Age", "Name", "Place", "Education", "Height"]

    df1 = spark.createDataFrame(data=student_data1, schema= details1)
    df2 = spark.createDataFrame(data=student_data2, schema=details2)
    # df1.show()
    # df2.show()
    df1 = df1.withColumn("Height", lit(5.1))
    df = df1.union(df2)
    df.show()

