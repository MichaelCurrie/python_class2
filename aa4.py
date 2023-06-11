"""
Visualize stock prices
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import mplfinance as mpf
import code

# Import necessary libraries
import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbol
tickerSymbol = "MSFT"

# Get data for this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
endDate = datetime.today().strftime("%Y-%m-%d")
startDate = (datetime.today() - timedelta(days=5 * 365)).strftime("%Y-%m-%d")

# Get historical data
ticker_df = tickerData.history(period="1d", start=startDate, end=endDate)

if False:
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=ticker_df, x=ticker_df.index, y="Close")
    plt.title("Microsoft Corp. (MSFT) closing price history")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.show()

code.interact(local=locals())


mpf.plot(
    ticker_df.iloc[:50, :],
    type="candle",
    style="charles",
    title="Microsoft Corp. (MSFT)",
    ylabel="Price ($)",
)
