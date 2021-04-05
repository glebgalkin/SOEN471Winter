from functools import reduce
import plotly.graph_objects as go

from pyspark.sql import Row
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

import matplotlib.pyplot as plt
import numpy as np
from pyspark.sql.functions import col
import pyspark.sql.functions as sql_func
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType, FloatType, BooleanType

from prediction_magic.dataset_trims import original_columns, daylight_colums, road_poi


def init_spark():
    spark = SparkSession \
        .builder \
        .master('local[*]')\
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .config("spark.driver.memory", "15g")\
        .getOrCreate()
    return spark


def read_dataset(filename):
    spark = init_spark()
    schema = StructType([StructField('ID', StringType(), True),
                         StructField('Source', StringType(), True),
                         StructField('TMC', StringType(), True),
                         StructField('Severity', IntegerType(), True),
                         StructField('Start_Time', TimestampType(), True),
                         StructField('End_Time', TimestampType(), True),
                         StructField('Start_Lat', FloatType(), True),
                         StructField('Start_Lng', FloatType(), True),
                         StructField('End_Lat', FloatType(), True),
                         StructField('End_Lng', FloatType(), True),
                         StructField('Distance(mi)', FloatType(), True),
                         StructField('Description', StringType(), True),
                         StructField('Number', StringType(), True),
                         StructField('Street', StringType(), True),
                         StructField('Side', StringType(), True),
                         StructField('City', StringType(), True),
                         StructField('County', StringType(), True),
                         StructField('State', StringType(), True),
                         StructField('Zipcode', StringType(), True),
                         StructField('Country', StringType(), True),
                         StructField('Timezone', StringType(), True),
                         StructField('Airport_Code', StringType(), True),
                         StructField('Weather_Timestamp', TimestampType(), True),
                         StructField('Temperature(F)', FloatType(), True),
                         StructField('Wind_Chill(F)', FloatType(), True),
                         StructField('Humidity(%)', FloatType(), True),
                         StructField('Pressure(in)', FloatType(), True),
                         StructField('Visibility(mi)', FloatType(), True),
                         StructField('Wind_Direction', StringType(), True),
                         StructField('Wind_Speed(mph)', FloatType(), True),
                         StructField('Precipitation(in)', FloatType(), True),
                         StructField('Weather_Condition', StringType(), True),
                         StructField('Amenity', BooleanType(), True),
                         StructField('Bump', BooleanType(), True),
                         StructField('Crossing', BooleanType(), True),
                         StructField('Give_Way', BooleanType(), True),
                         StructField('Junction', BooleanType(), True),
                         StructField('No_Exit', BooleanType(), True),
                         StructField('Railway', BooleanType(), True),
                         StructField('Roundabout', BooleanType(), True),
                         StructField('Station', BooleanType(), True),
                         StructField('Stop', BooleanType(), True),
                         StructField('Traffic_Calming', BooleanType(), True),
                         StructField('Traffic_Signal', BooleanType(), True),
                         StructField('Turning_Loop', BooleanType(), True),
                         StructField('Sunrise_Sunset', StringType(), True),
                         StructField('Civil_Twilight', StringType(), True),
                         StructField('Nautical_Twilight', StringType(), True),
                         StructField('Astronomical_Twilight', StringType(), True)])
    total_accidents_data = spark.read.schema(schema).csv(filename, header=True, mode="DROPMALFORMED", encoding="ISO-8859-1", inferSchema=True)
    # dropped meaningless and 1 class only columns
    final_result = total_accidents_data.drop('Country').drop('Turning_Loop').drop('id', 'Source', 'TMC', 'Description')\
        .withColumn('start_year', sql_func.date_format(total_accidents_data.Start_Time, 'y'))
    final_result = final_result.filter(((col('start_year') == 2019) | (col('start_year') == 2020)))
    final_result.show()
    print(final_result.count())
    return final_result


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


def build_states_graph(df):
    data = df.groupBy("State").count().filter(col('State') != 'null').collect()
    states = [row['State'] for row in data]
    state_counts = [row['count'] for row in data]
    print(type(states))
    print(states)

    fig = go.Figure(
        data=go.Choropleth(
            locations = states,
            z = state_counts,
            locationmode = 'USA-states',
            colorscale = 'SunsetDark',
            colorbar_title = "Count"),
        layout=go.Layout(
            title_text='US Accidents by State (Feb 2016—Dec 2020)',
            title_x=0.5,
            font=dict(family='Verdana', size=12, color='#000000'),
            geo_scope='usa'))

    fig.show()