def build_graph(df):
    df.groupBy("State").count().filter(col(column_name) != 'null').show()
    fig = go.Figure(
        data=go.Choropleth(
            locations = df.groupBy("State").count().filter(col(column_name) != 'null').collect(),
            z = pd.value_counts(df['State']).values.astype(float),
            locationmode = 'USA-states',
            colorscale = 'SunsetDark',
            colorbar_title = "Count"),
        layout=go.Layout(
            title_text='US Accidents by State (Feb 2016—Dec 2020)',
            title_x=0.5,
            font=dict(family='Verdana', size=12, color='#000000'),
            geo_scope='usa'))

    fig.show()