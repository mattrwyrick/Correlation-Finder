import os

from pathlib import Path


FILE_DIR = Path(__file__)
PROJ_DIR = FILE_DIR.parent
SRC_DIR = PROJ_DIR.parent
ROOT_DIR = SRC_DIR.parent
DATA_DIR = os.path.join(ROOT_DIR, "data")

SEED = 6687651975
YFINANCE_COLUMNS = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

YFINANCE_CORRELATION_COLUMNS = ["H/L Mean", "O/C Mean"]

CORRELATION_TOLERANCE = .75
INVERSE_CORRELATION_TOLERANCE = CORRELATION_TOLERANCE * -1.0
