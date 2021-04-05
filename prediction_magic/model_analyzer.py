from pyspark.ml.base import Estimator
from pyspark.ml.evaluation import RegressionEvaluator, MulticlassClassificationEvaluator
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, FeatureHasher
from pyspark.ml.pipeline import Pipeline
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.mllib.linalg import DenseVector
from pyspark.sql import DataFrame
from collections import namedtuple

from pyspark.sql.types import Row


class ModelAnalyzer:
    def __init__(self, dataframe, label_to_predict, seed, categorical_features, continuous_features):
        dataframe = dataframe.select(label_to_predict, *categorical_features, *continuous_features).dropna()
        dataframe.describe().show()
        label_features_df = self.prepare_df_for_prediction(dataframe, label_to_predict, categorical_features, continuous_features)
        (training, test) = label_features_df.randomSplit([0.8, 0.2], seed)
        self.__training_set = training
        self.__test_set = test
        self.__label_to_predict = label_to_predict
        self.__categorical_features = categorical_features
        self.__continuous_features = continuous_features

    def prepare_df_for_prediction(self, dataframe: DataFrame, label_to_predict, categorical_features, continuous_features):
        # stages = self.build_pipeline_stages(categorical_features, continuous_features)
        # pipelined_dataframe = self.pipeline_dataframe(stages, dataframe)
        hasher = FeatureHasher(inputCols=[*categorical_features, *continuous_features], outputCol='features')
        featurized = hasher.transform(dataframe)
        label_features = featurized.select(label_to_predict, 'features').withColumnRenamed(label_to_predict, 'label')
        return label_features

    def build_pipeline_stages(self, categorical_features, continuous_features):
        stages = []
        for categoricalCol in categorical_features:
            stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol + "Index")
            encoder = OneHotEncoder(inputCols=[stringIndexer.getOutputCol()],
                                    outputCols=[categoricalCol + "classVec"])
            stages += [stringIndexer, encoder]

        assemblerInputs = [c + "classVec" for c in categorical_features] + continuous_features
        assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
        stages += [assembler]
        return stages

    def pipeline_dataframe(self, stages, dataframe):
        print(stages)
        dataframe.printSchema()
        pipeline = Pipeline(stages=stages)
        pipelineModel = pipeline.fit(dataframe)
        model = pipelineModel.transform(dataframe)
        return model

    def train_test_evaluate_regression(self, regression_estimator: Estimator):
        regression_model = regression_estimator.fit(self.__training_set)
        predictions = regression_model.transform(self.__test_set)
        predictions.show()
        return self.__produce_regression_metrics(predictions)

    def __produce_regression_metrics(self, predictions: DataFrame):
        # evaluator = RegressionEvaluator(metricName="rmse", labelCol='label', predictionCol="prediction")
        # rmse = evaluator.evaluate(predictions, {evaluator.metricName: "rmse"})
        # return rmse
        evaluator = MulticlassMetrics(metricName='accuracy', labelCol='label', predictionCol='prediction')
        return evaluator.evaluate(predictions)
