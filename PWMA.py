import numpy as np
from scipy.special import comb
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def pascals_weighted_moving_average(prices, row):
    prices = np.asarray(prices)

    # Generate Pascal's triangle weights for the given rows
    weights = np.array([comb(row - 1, i) for i in range(row)])

    # Normalize weights
    weights /= weights.sum()

    # Convolve prices with weights
    pwma = np.convolve(prices, weights, mode='valid')

    # Pad the beginning with NaN to match the input size
    return pwma


# Calculate PWMA with a window of 4
file_path = 'dataset.csv'
data = pd.read_csv(file_path)
prices = data['close']
pwma = pascals_weighted_moving_average(prices, row=4)

# Print the result
print("PWMA:", pwma)

# Draw PWMA
plt.figure(figsize=(10, 6))
plt.plot(pwma, label='PWMA', color='orange')
plt.title('Pascal’s Weighted Moving Average (PWMA)')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
