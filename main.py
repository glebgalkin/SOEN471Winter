from Experiments.duration_regression_analysis import test_date_time_only
from prediction_magic import dataset_trims
from util.helpers import read_dataset

seed = 777

total_accidents_data = read_dataset('data/US_Accidents_Dec20.csv')

# display_ratios(total_accidents_data)
test_date_time_only(total_accidents_data, seed)

# build_states_graph(total_accidents_data)
