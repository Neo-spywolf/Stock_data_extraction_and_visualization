import matplotlib.pyplot as plt

# Plot Tesla stock data and revenue
plt.figure(figsize=(12, 6))
plt.plot(tesla_data['Date'], tesla_data['Close'], label='Tesla Stock Close Price', color='blue')
plt.xlabel('Date')
plt.ylabel('Tesla Stock Close Price', color='blue')
plt.legend(loc='upper left')

# Create a secondary y-axis for revenue data
plt.twinx()
plt.plot(tesla_revenue['Date'], tesla_revenue['Revenue'], label='Tesla Annual Revenue', color='red')
plt.ylabel('Tesla Annual Revenue (Millions USD)', color='red')
plt.legend(loc='upper right')

plt.title('Tesla Stock Data and Annual Revenue (Up to June 2021)')
plt.show()
