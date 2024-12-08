import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data.csv')

# Plot data
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['value'], label='Value over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Data')
plt.legend()
plt.show()
