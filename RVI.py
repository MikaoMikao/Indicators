import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd


def relative_vigor_index(close, open, high, low, period=10):
    # Calculate weighted numerator and denominator
    a = close - open
    b = np.roll(a, 1)  # One bar prior
    c = np.roll(a, 2)  # Two bars prior
    d = np.roll(a, 3)  # Three bars prior
    numerator = (a + 2 * b + 2 * c + d) / 6

    e = high - low
    f = np.roll(e, 1)  # One bar prior
    g = np.roll(e, 2)  # Two bars prior
    h = np.roll(e, 3)  # Three bars prior
    denominator = (e + 2 * f + 2 * g + h) / 6

    # Compute SMA for numerator and denominator
    num_sma = np.convolve(numerator, np.ones(period) / period, mode='valid')
    den_sma = np.convolve(denominator, np.ones(period) / period, mode='valid')
    print("Numerator SMA:", num_sma)
    print("Denominator SMA:", den_sma)

    # Calculate RVI
    rvi = num_sma / den_sma

    # Calculate Signal Line
    i = np.roll(rvi, 1)  # One bar prior
    j = np.roll(rvi, 2)  # Two bars prior
    k = np.roll(rvi, 3)  # Three bars prior
    signal = (rvi + 2 * i + 2 * j + k) / 6

    return rvi, signal


# Example data
file_path = 'dataset.csv'
data = pd.read_csv(file_path)
close = data['close']
open = data['open']
high = data['high']
low = data['low']

# Calculate RVI and Signal Line
rvi, signal = relative_vigor_index(close, open, high, low, period=10)

# Print results
print("RVI:", rvi)
print("Signal Line:", signal)

# Plot RVI and Signal Line
plt.figure(figsize=(10, 6))
plt.plot(rvi, label='RVI', color='blue')
plt.plot(signal, label='Signal Line', color='orange')
plt.title('Relative Vigor Index (RVI)')
plt.xlabel('Days')
plt.ylabel('RVI Value')
plt.legend()
plt.grid()
plt.show()
