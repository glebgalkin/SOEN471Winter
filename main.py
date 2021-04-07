from Experiments.duration_regression_analysis import test_date_time_only
from prediction_magic import dataset_trims
from util.helpers import read_dataset
from util.piecharts import display_piechart_of_column

# Glebs inports:
# from g_tools.gleb_data_analysis import dataset_stats, dt_sample

from g_tools.gleb_data_analysis import find_uniqe_values_of_column

seed = 777

df = read_dataset('data/US_Accidents_Dec20.csv')

k = find_uniqe_values_of_column(df, 'Wind_Direction')


from pyspark.sql import functions as F
def correct_column_wind_direction(df):
    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'SSE', 'S').otherwise(df['Wind_Direction']))
    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'WNW', 'W').otherwise(df['Wind_Direction']))

    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'WSW', 'W').otherwise(df['Wind_Direction']))
    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'NNW', 'N').otherwise(df['Wind_Direction']))
    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'ENE', 'E').otherwise(df['Wind_Direction']))

    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'SSW', 'S').otherwise(df['Wind_Direction']))

    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'West', 'W').otherwise(df['Wind_Direction']))
    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'ESE', 'E').otherwise(df['Wind_Direction']))
    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'North', 'N').otherwise(df['Wind_Direction']))

    df = df.withColumn('Wind_Direction',
                       F.when(df['Wind_Direction'] == 'VAR', 'Variable').otherwise(df['Wind_Direction']))

    df.show()
    return df


df = correct_column_wind_direction(df)

'''

df.show()

print(k)
'''
