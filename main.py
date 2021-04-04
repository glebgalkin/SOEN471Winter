from Experiments.duration_regression_analysis import test_date_time_only
from util.helpers import display_piechart_of_column, read_dataset, build_states_graph

seed = 777

total_accidents_data = read_dataset('data/US_Accidents_Dec20.csv')
total_accidents_data.show()
# display_ratios(total_accidents_data)

test_date_time_only(total_accidents_data, seed)

build_states_graph(total_accidents_data)
