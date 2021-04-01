from pyspark.sql import DataFrame
from pyspark.sql.functions import date_format

from prediction_magic.classification_analysis import ClassifierAnalyst
from prediction_magic.dataset_trims import no_weather, add_traffic_duration, add_start_month_day_hour_minutes
from prediction_magic.regressions import build_GeneralizedLinearRegressionModel
from util.data_analysis import display_ratios
from util.helpers import display_piechart_of_column, read_dataset

seed = 777

total_accidents_data = read_dataset('data/US_Accidents_Dec20.csv')
total_accidents_data.show()
# display_ratios(total_accidents_data)

total_accidents_data = add_traffic_duration(total_accidents_data)
total_accidents_data = add_start_month_day_hour_minutes(total_accidents_data)
total_accidents_data.show()

# analyst = ClassifierAnalyst(total_accidents_data, 'traffic_duration', seed)
# metrics = analyst.train_test_evaluate_regression(
#     lambda training_set, prediction_col: build_GeneralizedLinearRegressionModel(training_set, prediction_col))
# print(metrics)
