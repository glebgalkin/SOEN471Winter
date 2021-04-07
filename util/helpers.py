from pyspark.sql import SparkSession

import numpy as np
from pyspark.sql.functions import col
import pyspark.sql.functions as sql_func
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType, FloatType, BooleanType

from prediction_magic.dataset_trims import original_columns, daylight_colums, road_poi


def init_spark():
    spark = SparkSession \
        .builder \
        .master('local[*]') \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .config("spark.driver.memory", "15g") \
        .getOrCreate()
    return spark


def read_dataset(filename):
    spark = init_spark()
    total_accidents_data = spark.read.csv(filename, header=True, mode="DROPMALFORMED",
                                          encoding="ISO-8859-1", inferSchema=True)
    # dropped meaningless and 1 class only columns
    final_result = total_accidents_data.drop('Country').drop('id')\
        .withColumn('year', sql_func.date_format(total_accidents_data.Start_Time, 'y'))
    final_result = final_result.filter(col('State') == 'CA').filter((col('year') == 2019) |
                                                                    ((col('year') == 2020)))

    final_result.show()
    return final_result
