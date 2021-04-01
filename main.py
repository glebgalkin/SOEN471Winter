from pyspark.sql import DataFrame
from pyspark.sql.functions import date_format

from prediction_magic.classification_analysis import ClassifierAnalyst
from prediction_magic.dataset_trims import no_weather
from prediction_magic.regressions import build_GeneralizedLinearRegressionModel
from util.data_analysis import display_ratios
from util.helpers import display_piechart_of_column, read_dataset

seed = 777
original_columns = ['ID', 'Source', 'TMC', 'Severity',
                    'Start_Time', 'End_Time',
                    'Start_Lat', 'Start_Lng', 'End_Lat', 'End_Lng', 'Distance(mi)',
                    'Description', 'Number', 'Street', 'Side', 'City', 'County', 'State', 'Zipcode', 'Country',
                    'Timezone', 'Airport_Code',
                    'Weather_Timestamp', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)', 'Pressure(in)', 'Visibility(mi)',
                    'Wind_Direction', 'Wind_Speed(mph)', 'Precipitation(in)', 'Weather_Condition',
                    'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop',
                    'Traffic_Calming', 'Traffic_Signal', 'Turning_Loop',
                    'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight']


def add_time_formatted_columns(dataframe: DataFrame) -> DataFrame:
    date_format_template = 'M-d-H'
    temp = dataframe.withColumn('start_mm_dd_hh', date_format(total_accidents_data.Start_Time, date_format_template))
    temp = temp.withColumn('end_mm_dd_hh', date_format(total_accidents_data.End_Time, date_format_template))
    return temp


total_accidents_data = read_dataset('data/US_Accidents_Dec20.csv')
no_weather(total_accidents_data).show()
# display_ratios(total_accidents_data)
total_accidents_data = add_time_formatted_columns(total_accidents_data).show()

analyst = ClassifierAnalyst(total_accidents_data, 'traffic_duration', seed)
metrics = analyst.train_test_evaluate_regression(
    lambda training_set, prediction_col: build_GeneralizedLinearRegressionModel(training_set, prediction_col))
print(metrics)
