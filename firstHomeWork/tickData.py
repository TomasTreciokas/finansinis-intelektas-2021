import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

csv_data = pd.read_csv('../resource/EFA.USUSD_Ticks_17.02.2021-17.02.2021.csv')
csv_data['Local time'] = pd.to_datetime(csv_data['Local time'], format="%d.%m.%Y %H:%M:%S.%f GMT+0200")
csv_data = csv_data.set_index('Local time')

rowCount = csv_data.shape[0] + 1
x = np.array(range(1, rowCount))
csv_data['Indeksas'] = x
csv_data = csv_data.set_index('Indeksas')

plt.plot(csv_data.head(100))
plt.legend(['Ask', 'Bid'])
plt.xlabel('Kiekis')
plt.ylabel('Kaina')
plt.grid()
plt.show()
# plt.close()