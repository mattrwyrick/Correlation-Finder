import os
import pandas as pd

from correlation_finder.settings import DATA_DIR


SPY_PATH = os.path.join(DATA_DIR, "S&P by Weight.csv")


def load_spy_tickers():
    """
    Load the tickers from the S&P 500
    :return:
    """
    df = pd.read_csv(SPY_PATH)
    tickers = df["Symbol"]
    return tickers







