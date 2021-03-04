import pandas as pd


data = pd.read_csv('../resource/EFA.USUSD_Ticks_17.02.2021-17.02.2021.csv')
data['Local time'] = pd.to_datetime(data['Local time'], format="%d.%m.%Y %H:%M:%S.%f GMT+0200")
data['data'] = data['Local time']
data = data.set_index('Local time')

data['nextDate'] = data['data'].shift(-1)
data = data[:-1]
data['diff'] = pd.to_datetime(data['nextDate']) - pd.to_datetime(data['data'])
data = data.sort_values(by='diff', ascending=False)
print(data[:10])
