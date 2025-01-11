import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def chande_forecast_oscillator(prices, period):
    prices = np.asarray(prices)
    cfo = np.full(len(prices), np.nan)  # Initialize with NaN for padding

    for i in range(period - 1, len(prices)):
        # Get the window of prices
        y = prices[i - period + 1:i + 1]
        x = np.arange(len(y))  # Independent variable

        # Perform linear regression: y = mx + b
        m, b = np.polyfit(x, y, 1)  # Slope (m) and intercept (b)

        # Forecasted price for the last point in the window
        forecast = m * (len(y) - 1) + b

        # Calculate CFO
        cfo[i] = ((prices[i] - forecast) * 100 / prices[i])

    return cfo

# Calculate CFO with a period of 10
file_path = 'dataset.csv'
data = pd.read_csv(file_path)
prices = data['close']
cfo = chande_forecast_oscillator(prices,period=10)
print("CFO:", cfo)

# Plot CFO
import matplotlib.pyplot as plt

# Plot CFO along with prices
plt.figure(figsize=(10, 6))
plt.plot(cfo, label='Chande Forecast Oscillator (CFO)', color='orange')
plt.title('Chande Forecast Oscillator (CFO)')
plt.xlabel('Time')
plt.ylabel('CFO Value')
plt.legend()
plt.grid()
plt.show()
