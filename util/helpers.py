from functools import reduce

from pyspark.sql import Row
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

import matplotlib.pyplot as plt
import numpy as np
from pyspark.sql.functions import col

def init_spark():
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    return spark


def read_dataset(filename):
    spark = init_spark()
    total_accidents_data = spark.read.csv(filename, header=True, mode="DROPMALFORMED", encoding="ISO-8859-1")
    return total_accidents_data


def display_piechart_of_column(accidents_dataframe: DataFrame, column_name: str):
    counted_accidents = accidents_dataframe.groupBy(column_name).count().filter(col(column_name) != 'null').collect()

    labels = [label[column_name] for label in counted_accidents]
    counts = [label['count'] for label in counted_accidents]
    count_sum = reduce(lambda x, y: x + y, counts)
    percentages = [count/count_sum for count in counts]
    piechart(labels, percentages, column_name)


def piechart(labels, percentages, column_name):
    plt.pie(percentages, labels=labels)
    plt.title(f'ratio by {column_name}')
    plt.show()
