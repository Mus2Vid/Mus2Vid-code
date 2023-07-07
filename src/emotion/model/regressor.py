from sklearn.svm import SVR
import os
import joblib


MODEL_DIR = "./models/emotion"
MODEL_EXT = "model"


class EmotionRegressor():

    def __init__(self, epsilon=0.2):
        self.svr = SVR(epsilon=epsilon)

    def fit(self, features, targets):
        self.svr.fit(features, targets)

    def predict(self, inputs):
        return self.svr.predict(inputs)

    def save(self, filename):
        if not os.path.exists(MODEL_DIR): os.mkdir(MODEL_DIR)
        joblib.dump(self.svr, f"{MODEL_DIR}/{filename}.{MODEL_EXT}")

    def load(self, filename):
        self.svr = joblib.load(f"{MODEL_DIR}/{filename}.{MODEL_EXT}") 


if __name__ == "__main__":
    pass