import yfinance as yf

# Create a ticker object for Tesla
ticker_tsla = yf.Ticker("TSLA")

# Extract Tesla stock data with a period of 'max'
tesla_data = ticker_tsla.history(period="max")

# Reset the index
tesla_data.reset_index(inplace=True)

# Display the first five rows of the tesla_data dataframe
print(tesla_data.head())
