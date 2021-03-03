import matplotlib.pyplot as plt
import pandas as pd


csv_data = pd.read_csv('../resource/2628.HKHKD_Candlestick_1_M_BID_10.02.2021-27.02.2021.csv')
csv_data['Gmt time'] = pd.to_datetime(csv_data['Gmt time'], format="%d.%m.%Y %H:%M:%S.%f")
csv_data = csv_data.set_index('Gmt time')

plt.plot(csv_data.head(100))
plt.grid()
plt.legend(['Open', 'Low', 'High', 'Close'])
plt.xlabel('Laikas')
plt.ylabel('Kaina')
plt.show()
# plt.close()