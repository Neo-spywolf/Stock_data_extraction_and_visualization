# Create a ticker object for GameStop
ticker_gme = yf.Ticker("GME")

# Extract GameStop stock data with a period of 'max'
gme_data = ticker_gme.history(period="max")

# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows of the gme_data dataframe
print(gme_data.head())

