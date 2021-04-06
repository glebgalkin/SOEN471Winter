from Experiments.duration_regression_analysis import test_date_time_only
from prediction_magic import dataset_trims
from util.helpers import read_dataset
from util.piecharts import display_piechart_of_column

# Glebs inports:
# from g_tools.gleb_data_analysis import dataset_stats, dt_sample


seed = 777

# total_accidents_data = read_dataset('data/US_Accidents_Dec20.csv')

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
filename = "Data/US_Accidents_Dec20.csv"
lines = spark.sparkContext.textFile(filename)
lines.show()
