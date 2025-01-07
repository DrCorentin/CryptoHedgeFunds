import os
import pandas as pd
import numpy as np

def calculate_returns(df, initial_capital_eur, initial_capital_btc):
  # Calculate returns in EUR, BTC, and percentage
  df['Return_EUR'] = (df['Close'] / df['Close'][0]) * initial_capital_eur
  df['Return_BTC'] = (df['Close'] / df['Close'][0]) * initial_capital_btc
  df['Percentage_Return'] = ((df['Close'] / df['Close'][0]) - 1) * 100
  return df
  
def ensure_directories():
    os.makedirs("data/logs", exist_ok=True)
    os.makedirs("data/historical", exist_ok=True)
