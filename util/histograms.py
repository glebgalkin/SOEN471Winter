import matplotlib.pyplot as plt
from pyspark.sql.functions import concat_ws, col
import numpy

# def show_histogram(dataframe):
#     dataframe = dataframe.select('month', concat_ws('_', 'day', 'hour_minutes').alias('timestamp'), 'traffic_duration')
#     dataframe = dataframe.filter(dataframe.month == 1).drop('month').orderBy('traffic_duration', ascending=False)
#     dataframe.show(1000)
#     dataframe.describe().show()
#     print(dataframe.count())
#     print('long')
#
#     print('built bins')
#     plt.figure(figsize=(20,10))
#     plt.hist(, bins = 5000)
#     print('hist completed, showing')
#     plt.show()
