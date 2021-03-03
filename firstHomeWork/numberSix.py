import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../resource/2628.HKHKD_Candlestick_1_M_BID_10.02.2021-27.02.2021.csv')
data['Gmt time'] = pd.to_datetime(data['Gmt time'], format="%d.%m.%Y %H:%M:%S.%f")
data['data'] = data['Gmt time']
data = data.set_index('Gmt time')

data['Hour'] = data['data'].dt.hour
sorted_data_tick = data[data.Hour > 8]
sorted_data_tick = sorted_data_tick[sorted_data_tick.Hour < 10]

plt.title('awdawd')
plt.ylabel("Kaina")
ax = plt.gca()
for column in ['Open', 'High', 'Low', 'Close']:
    sorted_data_tick.plot(kind='line', x='data', y=column, ax=ax)
plt.grid(True)
plt.show()
