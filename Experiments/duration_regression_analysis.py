from pyspark.ml.regression import GeneralizedLinearRegression, LinearRegression, DecisionTreeRegressor, \
    RandomForestRegressor
from pyspark.sql import DataFrame

from prediction_magic import dataset_trims
from prediction_magic.dataset_trims import road_poi
from prediction_magic.model_analyzer import ModelAnalyzer
from prediction_magic.regressions import build_GeneralizedLinearRegressionModel


def test_date_time_only(total_accidents_data: DataFrame, seed: int):
    total_accidents_data = dataset_trims.add_traffic_duration(total_accidents_data)
    total_accidents_data = dataset_trims.add_start_month_day_hour_minutes(total_accidents_data)

    analyst = ModelAnalyzer(total_accidents_data, 'traffic_duration', seed, ['Weather_Condition'],
                            ['hour_minutes', 'month', 'day', 'Start_Lat', 'Start_Lng'])
    metrics = analyst.train_test_evaluate_regression(LinearRegression(maxIter=2))
    print(metrics)
    metrics = analyst.train_test_evaluate_regression(LinearRegression(maxIter=1))
    print(metrics)

    analyst = ModelAnalyzer(total_accidents_data, 'traffic_duration', seed, ['Weather_Condition'],
                            ['hour_minutes', 'month', 'day', 'Start_Lat', 'Start_Lng'])
    metrics = analyst.train_test_evaluate_regression(DecisionTreeRegressor())
    print(metrics)
    metrics = analyst.train_test_evaluate_regression(RandomForestRegressor())
    print(metrics)
    print('done working')
