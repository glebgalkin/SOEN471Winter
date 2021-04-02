from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import DataFrame
from collections import namedtuple


class ClassifierAnalyst:
    def __init__(self, dataframe, label_to_predict, seed):
        (training, test) = dataframe.randomSplit([0.8, 0.2], seed)
        self.__training_set = training
        self.__test_set = test
        self.__label_to_predict = label_to_predict

    def train_test_evaluate_regression(self, model_trainer):
        model = model_trainer(self.__training_set, self.__label_to_predict)
        predictions = model.transform(self.__test_set)
        predictions.show()
        return self.__produce_regression_metrics(predictions)

    def __produce_regression_metrics(self, predictions: DataFrame):
        evaluator = RegressionEvaluator(metricName="rmse", labelCol=self.__label_to_predict, predictionCol="prediction")

        rmse = evaluator.evaluate(predictions, {evaluator.metricName: "rmse"})
        r2 = evaluator.evaluate(predictions, {evaluator.metricName: "r2"})

        RegressionMetrics = namedtuple('RegressionMetrics', 'rmse, rse')
        return RegressionMetrics(rmse, r2)
