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

from sklearn.model_selection import GridSearchCV

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    """
    Evaluate the models using GridSearchCV and return a dictionary with model names and their best test R2 scores.
    """
    try:
        model_report = {}
        for name, model in models.items():
            param_grid = params.get(name, {})  # get params for this model, or empty dict
            if param_grid:
                gs = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, scoring='r2')
                gs.fit(X_train, y_train)
                best_model = gs.best_estimator_
            else:
                best_model = model
                best_model.fit(X_train, y_train)
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            model_report[name] = test_model_score
        return model_report
    except Exception as e:
        raise CustomException(e, sys)