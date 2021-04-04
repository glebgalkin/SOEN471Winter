from pyspark.sql import DataFrame
from pyspark.sql.functions import date_format, col
import plotly.graph_objects as go

from Experiments.duration_regression_analysis import test_date_time_only
from prediction_magic.classification_analysis import ClassifierAnalyst
from prediction_magic import dataset_trims
from prediction_magic.regressions import build_GeneralizedLinearRegressionModel
from util.data_analysis import display_ratios
from util.helpers import display_piechart_of_column, read_dataset

seed = 777

total_accidents_data = read_dataset('data/US_Accidents_Dec20.csv')

# # display_ratios(total_accidents_data)
#
# test_date_time_only(total_accidents_data, seed)

def build_graph(df):
    data = df.groupBy("State").count().filter(col('State') != 'null').collect()
    states = [row['State'] for row in data]
    state_counts = [row['count'] for row in data]
    print(type(states))
    print(states)

    fig = go.Figure(
        data=go.Choropleth(
            locations = states,
            z = state_counts,
            locationmode = 'USA-states',
            colorscale = 'SunsetDark',
            colorbar_title = "Count"),
        layout=go.Layout(
            title_text='US Accidents by State (Feb 2016—Dec 2020)',
            title_x=0.5,
            font=dict(family='Verdana', size=12, color='#000000'),
            geo_scope='usa'))

    fig.show()

build_graph(total_accidents_data)
