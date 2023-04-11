"""main"""
from app.get_history.get_history import pars_history


BASE_CURRENCIES='usdt'
STORAGE = r'C:PATH'

if __name__ == "__main__":
    pars_history(BASE_CURRENCIES, STORAGE)
