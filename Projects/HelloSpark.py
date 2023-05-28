import sys

from pyspark.sql import *
from lib.utils import load_survey_details
from lib.logger import Log4J

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Hello Spark")\
            .master("local[3]")\
            .getOrCreate()
    logger = Log4J(spark)

    if len(sys.argv) !=2:
        logger.error("Usage: HelloSpark <filename>")
        sys.exit(-1)

    df_file = load_survey_details(spark, sys.argv[1])

    df_file.createOrReplaceTempView("survey_tbl")
    filtered_df_file = spark.sql("select country, count(1) as count from survey_tbl where Age<40 group by Country")

    filtered_df_file.show()