# Statistical Properties of PySpark Dataframe
from pyspark.sql import DataFrame

"""
Output:
+ — — — -+ — — — — — — — — -+
|summary| age|
+ — — — -+ — — — — — — — — -+
| count| 400|
| mean|51.48337595907928|
| stddev|17.16971408926224|
| min| 11|
| max| ?|
+ — — — -+ — — — — — — — — -+
"""


def dataset_stats(df: DataFrame, column_name: str):
    df.describe([column_name]).show()


# Function that removes useless columns
def remove_useless_columns(df: DataFrame):
    useless_columns = ['ID', 'Source', 'TMC', 'Description']
    df = df.drop(*useless_columns)

    return df


# Finding unique values of column
def find_uniqe_values_of_column(df: DataFrame, column_name: str):
    return df.select(column_name).distinct().rdd.map(lambda r: r[0]).collect()


# Filtering out specific value from specific column
def filter_out_value_from_column(df: DataFrame, column_name: str, value):
    df = df.filter(df[column_name] == value)
    return df


# Count missing values in a column
def count_missing_values_in_column(df: DataFrame, column_name: str):
    return df.filter(df[column_name].isNull()).count()


# Fill missing values using mean of the column of PySpark Dataframe:


# Find the avg of all numeric columns
from pyspark.sql.functions import avg
def mean_of_pyspark_columns(df, numeric_cols, verbose=False):
    col_with_mean = []
    for col in numeric_cols:
        mean_value = df.select(avg(df[col]))
        avg_col = mean_value.columns[0]
        res = mean_value.rdd.map(lambda row: row[avg_col]).collect()

        if (verbose == True): print(mean_value.columns[0], "\t", res[0])
        col_with_mean.append([col, res[0]])
    return col_with_mean


# Fill missing values for mean
from pyspark.sql.functions import when, lit
def fill_missing_with_mean(df, numeric_cols):
    col_with_mean = mean_of_pyspark_columns(df, numeric_cols)

    for col, mean in col_with_mean:
        df = df.withColumn(col, when(df[col].isNull() == True,
                                     lit(mean)).otherwise(df[col]))

    return df


def calculate_feature_and_missing_percentage(df: DataFrame, k: list ):
    return 0
