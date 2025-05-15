import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score

def save_object(file_path, obj):

    """
    Save the object to a file using pickle.
    """
    
    try:
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
        print(f"Object saved to {file_path}")
    except Exception as e:
        print(f"Error saving object: {e}")

def evaluate_models(X_train, y_train, X_test, y_test, models):
    """
    Evaluate the models and return a dictionary with model names and their test R2 scores.
    """
    try:
        model_report = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            model_report[name] = test_model_score
        return model_report
    except Exception as e:
        raise CustomException(e, sys)