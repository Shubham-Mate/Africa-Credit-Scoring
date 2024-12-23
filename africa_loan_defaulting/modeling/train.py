from pathlib import Path
from tqdm import tqdm
from africa_loan_defaulting.config import MODELS_DIR, PROCESSED_DATA_DIR, MODEL_NAME
from xgboost import XGBClassifier
import pickle
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import logging

logging.basicConfig(level=logging.DEBUG, force=True)

def train(train_X, train_Y, test_X=None, test_Y=None):
    model = XGBClassifier(objective='binary:logistic')
    model.fit(train_X, train_Y)
    pickle.dump(model, open(MODELS_DIR / MODEL_NAME, "wb"))
    logging.info("Successfully trained and saved model")

    train_preds = model.predict(train_X)
    logging.info(f'Train set:\n \
        Accuracy Score: {accuracy_score(train_Y, train_preds)},\n \
        Recall Score: {recall_score(train_Y, train_preds)},\n \
        Precision Score: {precision_score(train_Y, train_preds)},\n \
        F1 Score: {f1_score(train_Y, train_preds)}\n')
    
    if test_X is not None and test_Y is not None:
        test_preds = model.predict(test_X)
        logging.info(f'Train set:\n \
        Accuracy Score: {accuracy_score(test_Y, test_preds)},\n \
        Recall Score: {recall_score(test_Y, test_preds)},\n \
        Precision Score: {precision_score(test_Y, test_preds)},\n \
        F1 Score: {f1_score(test_Y, test_preds)}\n') 
    