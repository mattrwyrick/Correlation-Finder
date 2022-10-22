import os
import pandas as pd
import datetime

from correlation_finder.tools import (
    get_datetime_range,
    correlate,
    interpret_correlation_coefficient,
    normalize_column,
    download_stock_price
)

from correlation_finder.settings import DATA_DIR
from correlation_finder.data import load_spy_tickers
from correlation_finder.experiments import portfolio_correlation


from scipy.stats import pearsonr



COLUMNS = [
    "H/L Mean",
    "O/C Mean",
    "High",
    "Low",
    "Open",
    "Close",
    "Adj Close",
    "Volume"
]

TICKER_PAIRS = [
    ("ISRG", "PFE"),  # Intuitive Surgical Inc. and Pfizer
    ("AAPL", "DE"),   # Apple and John Deere
    ("BRK-B", "SPY"),  # Berkshire Hathaway and S&P 500
]


# SELECT

TICKER_1, TICKER_2 = TICKER_PAIRS[1]
COLUMN = COLUMNS[5]
NORMALIZE = True

YEARS = 0
MONTHS = 6
WEEKS = 0


def main():
    """
    Run the experimentation
    :return:
    """
    start_dt, end_dt = get_datetime_range(years=YEARS, months=MONTHS, weeks=WEEKS)

    # correlation = correlate(COLUMN, TICKER_1, TICKER_2, start_dt, end_dt, NORMALIZE)
    # print_out_results(correlation)

    # df = pd.DataFrame()
    # tickers = load_spy_tickers()
    # ticker = " ".join(tickers)
    # df = download_stock_price(ticker, start_dt, end_dt)

    data = dict()
    spy_dir = os.path.join(DATA_DIR, "spy")
    for file_name in os.listdir(spy_dir):
        path = os.path.join(spy_dir, file_name)
        df = pd.read_csv(path, sep=",")
        df["H/L Mean"] = df[["High", "Low"]].mean(axis=1)
        df["O/C Mean"] = df[["Open", "Close"]].mean(axis=1)
        data[file_name.replace(".csv", "")] = df[COLUMN]


    ticker = "AAPL"
    x = data[ticker]

    results = list()

    for key in data:
        y = data[key]
        if x.shape != y.shape:
            continue

        r, _ = pearsonr(x, y)
        if abs(r) >= .75:
            results.append([r, key])

    results.sort(reverse=True)

    print(f"\n\n{ticker}\n")
    [print(f"{p[1]}:\t{round(p[0], 3)}") for p in results]


def print_out_results(r):
    """
    Print out the results from the experiment
    :param r:
    :return:
    """
    print("\n\n")
    print(f"Comparing {TICKER_1} and {TICKER_2}")
    print(f"on {COLUMN} for the last {YEARS} years, {MONTHS} months, {WEEKS} weeks")
    interpret_correlation_coefficient(r)


if __name__ == "__main__":
    main()

