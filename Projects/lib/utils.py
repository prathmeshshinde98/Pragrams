def load_survey_details(spark, data_file):
    return spark.read.option("Header", "True").option("inferScheme", "True").csv(data_file)