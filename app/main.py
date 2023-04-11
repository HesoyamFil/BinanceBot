"""main"""
import os
from get_history.get_history import limit, pars_history


BASE_CURRENCIES='usdt'
STORAGE = os.getenv('HISTORY_PATH')

if __name__ == "__main__":
    pars_history(BASE_CURRENCIES, STORAGE)
    limit()
