from pyspark.ml.regression import GeneralizedLinearRegression


def build_GeneralizedLinearRegressionModel(training_set, predictionCol):
    glr = GeneralizedLinearRegression(family="gaussian", link="identity", linkPredictionCol=predictionCol)
    glr.setMaxIter(10)
    model = glr.fit(training_set)
    return model
