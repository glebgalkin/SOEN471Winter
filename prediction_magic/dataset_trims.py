from pyspark.sql import DataFrame

def no_id_source_description(dataframe: DataFrame) -> DataFrame:
    return dataframe.drop('ID', 'Source', 'Description')

def no_weather(dataframe: DataFrame) -> DataFrame:
    return dataframe.drop()

def no_address(dataframe: DataFrame) -> DataFrame:
