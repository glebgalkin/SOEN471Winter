from util.data_analysis import display_ratios
from util.helpers import display_piechart_of_column, read_dataset

total_accidents_data = read_dataset('data/US_Accidents_Dec20.csv')
total_accidents_data.show()
# display_ratios(total_accidents_data)
model = build_end_time_prediction_model(total_accidents_data)