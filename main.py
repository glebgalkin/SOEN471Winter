from pyspark.sql import DataFrame
from pyspark.sql.functions import date_format

from Experiments.duration_regression_analysis import test_date_time_only
from prediction_magic.classification_analysis import ClassifierAnalyst
from prediction_magic import dataset_trims
from prediction_magic.regressions import build_GeneralizedLinearRegressionModel
from util.data_analysis import display_ratios
from util.helpers import display_piechart_of_column, read_dataset

seed = 777

total_accidents_data = read_dataset('data/US_Accidents_Dec20.csv')
# display_ratios(total_accidents_data)

test_date_time_only(total_accidents_data, seed)
