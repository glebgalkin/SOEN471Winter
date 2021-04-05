from pyspark.ml.regression import GeneralizedLinearRegression, LinearRegression
from pyspark.sql import DataFrame

from prediction_magic import dataset_trims
from prediction_magic.dataset_trims import road_poi
from prediction_magic.model_analyzer import ModelAnalyzer
from prediction_magic.regressions import build_GeneralizedLinearRegressionModel


def test_date_time_only(total_accidents_data: DataFrame, seed: int):
    total_accidents_data = dataset_trims.add_traffic_duration(total_accidents_data)
    total_accidents_data = dataset_trims.add_start_month_day_hour_minutes(total_accidents_data)

    analyst = ModelAnalyzer(total_accidents_data, 'traffic_duration', seed,
                            ['Civil_Twilight', 'Nautical_Twilight', 'Astronomical_Twilight', 'Sunrise_Sunset', 'Weather_Condition',
                             *road_poi],
                            ['hour_minutes', 'month', 'day', 'Start_Lat', 'Start_Lng'])
    metrics = analyst.train_test_evaluate_regression(LinearRegression(maxIter=10))
    print('done working')
    print(metrics)
