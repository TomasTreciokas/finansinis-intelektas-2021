import matplotlib.pyplot as plt
import pandas as pd

csv_data = pd.read_csv('../resource/2628.HKHKD_Candlestick_1_D_BID_10.02.2021-27.02.2021.csv')
csv_data['Gmt time'] = pd.to_datetime(csv_data['Gmt time'], format="%d.%m.%Y %H:%M:%S.%f")
csv_data = csv_data.set_index('Gmt time')
df = csv_data.drop(['Low', 'High'], 1)

plt.plot(df.head(1000))
plt.xticks(rotation=90)
plt.legend(['Close', 'Open'])
plt.xlabel('Laikas')
plt.ylabel('Kaina')
plt.grid()
plt.show()
# plt.close()