import plotly.graph_objects as go
from pyspark.sql.functions import col


def build_states_graph(df):
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