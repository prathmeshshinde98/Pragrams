

def filter_func(spark,file_read):
    return file_read.filter("Age > 40").select("Age", "Gender", "Country")