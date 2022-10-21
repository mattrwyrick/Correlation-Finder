import datetime

from correlation_finder.tools import (
    get_datetime_range,
    correlate,
    interpret_correlation_coefficient,
    normalize_column
)


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
COLUMN = COLUMNS[1]
NORMALIZE = True

YEARS = 0
MONTHS = 6
WEEKS = 0


def main():
    """
    Run the experimentation
    :return:
    """
    start_dt, end_dt = get_datetime_range(years=YEARS, months=MONTHS)
    correlation = correlate(COLUMN, TICKER_1, TICKER_2, start_dt, end_dt, NORMALIZE)
    print_out_results(correlation)


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

