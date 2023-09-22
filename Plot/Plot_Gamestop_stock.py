# Plot GameStop stock data and revenue
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot GameStop Stock Close Price on the primary y-axis (left)
ax1.plot(gme_data['Date'], gme_data['Close'], label='GameStop Stock Close Price', color='blue')
ax1.set_xlabel('Date')
ax1.set_ylabel('GameStop Stock Close Price', color='blue')
ax1.legend(loc='upper left')

# Create a secondary y-axis (right) for revenue data
ax2 = ax1.twinx()
ax2.plot(gme_revenue['Date'], gme_revenue['Revenue'], label='GameStop Annual Revenue', color='red')
ax2.set_ylabel('GameStop Annual Revenue (Millions USD)', color='red')
ax2.legend(loc='upper right')

# Set a title for the combined graph
plt.title('GameStop Stock Data and Annual Revenue (Up to June 2021)')

# Show the plot
plt.show()
