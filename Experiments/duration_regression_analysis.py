from pyspark.ml.regression import GeneralizedLinearRegression
from pyspark.sql import DataFrame

from prediction_magic import dataset_trims
from prediction_magic.classification_analysis import ClassifierAnalyst
from prediction_magic.regressions import build_GeneralizedLinearRegressionModel


def test_date_time_only(total_accidents_data: DataFrame, seed: int):
    total_accidents_data = dataset_trims.add_traffic_duration(total_accidents_data)
    total_accidents_data = dataset_trims.add_start_month_day_hour_minutes(total_accidents_data)
    total_accidents_data = total_accidents_data.drop(*dataset_trims.useless_columns)
    total_accidents_data = total_accidents_data.drop(*dataset_trims.weather_columns)
    total_accidents_data = total_accidents_data.drop(*dataset_trims.address_columns)
    total_accidents_data = total_accidents_data.drop(*dataset_trims.start_end_time_columns)
    total_accidents_data = total_accidents_data.drop(*dataset_trims.timezone_airport)
    total_accidents_data = total_accidents_data.drop(*['End_Lat', 'End_Lng', 'Distance(mi)'])

    total_accidents_data.show()

    analyst = ClassifierAnalyst(total_accidents_data, 'traffic_duration', seed)
    metrics = analyst.train_test_evaluate_regression(GeneralizedLinearRegression(family="gaussian", link='identity', maxIter=10))
    print('done working')
    print(metrics)
