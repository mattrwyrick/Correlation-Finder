import datetime
import pandas as pd
import numpy as np
import yfinance as yf

from scipy.stats import pearsonr

from correlation_finder.settings import CORRELATION_TOLERANCE, INVERSE_CORRELATION_TOLERANCE


def correlate(field, ticker_1, ticker_2, start_dt, end_dt, normalize=False):
    """
    Return the correlation coefficient between to stock prices
    :param field: str
    :param ticker_1: str
    :param ticker_2: str
    :param start_dt: datetime
    :param end_dt: datetime
    :return: float
    """
    df_1 = download_stock_price(ticker_1, start_dt, end_dt)
    df_2 = download_stock_price(ticker_2, start_dt, end_dt)

    if normalize:
        series_1 = normalize_column(df_1, field)
        series_2 = normalize_column(df_2, field)
    else:
        series_1 = df_1[field]
        series_2 = df_2[field]

    r, _ = pearsonr(series_1, series_2)

    return r


def interpret_correlation_coefficient(r, corr=CORRELATION_TOLERANCE, inv_corr=INVERSE_CORRELATION_TOLERANCE):
    """
    Print out the results
    :param r: float
    :param corr: float
    :param inv_corr: float
    :return:
    """
    r = round(r, 3)
    if r >= corr:
        print(f"The data is correlated: {r}")

    elif r <= inv_corr:
        print(f"The data is inversely correlated: {r}")

    else:
        print(f"There is no relationship: {r}")


def normalize_column(df, column):
    """
    Normalize the data in a given column
    :param df: dataframe
    :param column: str
    :return: dataframe
    """
    df[column] = np.divide(df[column], df[column].mean(axis=0))
    return df[column]


def download_stock_price(ticker, start_dt, end_dt):
    """
    Download the stock ticker price for the given date range
    :param ticker: str
    :param start_dt: datetime
    :param end_dt: datetime
    :return: dataframe
    """
    start, end = get_yfinance_date_range(start_dt, end_dt)

    df = yf.download(ticker, start, end)
    df.reset_index(inplace=True)

    df["H/L Mean"] = df[["High", "Low"]].mean(axis=1)
    df["O/C Mean"] = df[["Open", "Close"]].mean(axis=1)


    return df


def get_datetime_range(anchor_date=datetime.datetime.today(), years=0, months=0, weeks=0, historical=True):
    """
    Generate a datetime date range
    :param anchor_date: datetime
    :param years: int
    :param months: int
    :param weeks: int
    :param historical: bool
    :return: list of datetime [dt, dt]
    """
    days = 0
    days += 365.25 * years
    days += 30.5 * months
    days += 7 * weeks
    days = round(days)
    delta = datetime.timedelta(days=days)

    if historical:
        start_date = anchor_date - delta
        date_range = [start_date, anchor_date]
    else:
        end_date = anchor_date + delta
        date_range = [anchor_date, end_date]

    return date_range


def get_yfinance_date_range(start_date, end_date):
    """
    Return the date range for the Yahoo finance library
    :param start_date: datetime
    :param end_date: datetime
    :return:
    """
    start = f"{start_date.year}-{start_date.month}-{start_date.day}"
    end = f"{end_date.year}-{end_date.month}-{end_date.day}"
    date_range = [start, end]

    return date_range







