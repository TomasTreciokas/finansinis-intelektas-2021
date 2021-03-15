import matplotlib.pyplot as plt
import pandas as pd

start_date = '06/11/2020'
end_date = '03/12/2021'
title = 'Price channel'
file_name = '../resource/HistoricalData_apple.csv'
period = 20

data = pd.read_csv(file_name)
data['Time'] = pd.to_datetime(data['Time'], format="%Y.%m.%d")
data = data.set_index('Time')
data = data.iloc[::-1]

data['Highest'] = data['High'].rolling(period).max()
data['Lowest'] = data['Low'].rolling(period).min()

plot_data = data[['Highest', 'Lowest', 'Close']].loc[start_date:end_date]

plt.plot(plot_data)
plt.legend(['Highest', 'Lowest', 'Close'])
plt.ylabel('Close')
plt.xlabel('Time')
plt.xticks(rotation=45)
plt.grid()
plt.show()
