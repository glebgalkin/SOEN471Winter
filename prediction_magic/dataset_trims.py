from pyspark.sql import DataFrame
from pyspark.sql import functions as sql_func
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

original_columns = ['ID', 'Source', 'TMC', 'Severity', 'Description'
                    'Start_Time', 'End_Time',
                    'Start_Lat', 'Start_Lng', 'End_Lat', 'End_Lng', 'Distance(mi)',
                    'Number', 'Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country',
                    'Timezone', 'Airport_Code',
                    'Weather_Timestamp', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Direction', 'Wind_Speed(mph)', 'Precipitation(in)', 'Weather_Condition',
                    'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop',
                    'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']


useless_columns = ['ID', 'Source', 'TMC', 'Description']
start_end_time_columns = ['Start_Time', 'End_Time']
geo_location_columns = ['Start_Lat', 'Start_Lng', 'End_Lat', 'End_Lng', 'Distance(mi)']
address_columns = ['Number', 'Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country']
timezone_airport = ['Timezone', 'Airport_Code']
weather_columns = ['Weather_Timestamp', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Direction', 'Wind_Speed(mph)', 'Precipitation(in)', 'Weather_Condition']
road_poi = ['Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal']
daylight_colums = ['Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']

date_format_template = 'M-d-H-m'


def add_time_formatted_columns(dataframe: DataFrame) -> DataFrame:
    dataframe = dataframe.withColumn('start_mm_dd_hh', sql_func.date_format(dataframe.Start_Time, date_format_template))
    dataframe = dataframe.withColumn('end_mm_dd_hh', sql_func.date_format(dataframe.End_Time, date_format_template))
    return dataframe


def add_traffic_duration(dataframe: DataFrame) -> DataFrame:
    dataframe = add_time_formatted_columns(dataframe)
    dataframe = dataframe.withColumn('traffic_duration', (sql_func.unix_timestamp('End_Time', format=date_format_template) - sql_func.unix_timestamp('Start_Time', format=date_format_template))/60)
    return dataframe


def add_start_month_day_hour_minutes(dataframe):
    dataframe = dataframe.withColumn('month', sql_func.date_format(dataframe.Start_Time, 'M'))\
        .withColumn('month', col('month').cast(IntegerType()))
    dataframe = dataframe.withColumn('day', sql_func.date_format(dataframe.Start_Time, 'd'))\
        .withColumn('day', col('day').cast(IntegerType()))
    dataframe = dataframe.withColumn('hour_minutes', sql_func.date_format(dataframe.Start_Time, 'H')*60 + sql_func.date_format(dataframe.Start_Time, 'm'))
    return dataframe