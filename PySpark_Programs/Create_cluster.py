from pyspark.sql import *
import json
import requests
if __name__ == "__main__":
    spark = SparkSession.builder.appName("CreateCluster").master('local[3]').getOrCreate()

    api_key = ""
    city = ""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q":city, "appid":api_key, "units":"metrics"}

    response = requests.get(base_url)

    print(response.content)