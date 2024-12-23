from pathlib import Path
import pickle
import logging
from africa_loan_defaulting.config import MODELS_DIR, PROCESSED_DATA_DIR, MODEL_NAME
import pandas as pd

logging.basicConfig(level=logging.DEBUG, force=True)

def predict(X) -> pd.DataFrame:
    model = pickle.load(open(MODELS_DIR / MODEL_NAME, "rb"))
    logging.info("Model Successfully Loaded")
    predicted = model.predict(X)

    #submission = pd.DataFrame({
    #'ID': X['ID'],
    #'Target': predicted
    #})
    #submission = submission.set_index('ID')
    return predicted
