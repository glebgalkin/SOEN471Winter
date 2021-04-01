from pyspark.sql import DataFrame

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
road_specialties = ['Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop']
daylight_colums = ['Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']


def no_id_source_description(dataframe: DataFrame) -> DataFrame:
    return dataframe.drop(*useless_columns)


def no_weather(dataframe: DataFrame) -> DataFrame:
    return dataframe.drop(*weather_columns)


def no_address(dataframe: DataFrame) -> DataFrame:
    return dataframe.drop(*address_columns)
