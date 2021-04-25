import WilliamsR_strategy as WR_strategy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import thirdHomeWork.util as util
import WilliamsR_strategy as optimizationUtil


csv_data = pd.read_csv('../resource/HistoricalData_1618413252136.csv')
csv_data['Time'] = pd.to_datetime(csv_data['Time'], format="%Y.%m.%d")
csv_data = csv_data.set_index('Time')
csv_data = csv_data.iloc[::-1]
dates = pd.to_datetime(csv_data.index.values, format="%Y.%m.%d")

period = 40
take_profit = 10
bull_open = -50
bull_close = -20
starting_budget = 10000
stock_quantity = 15
expenses = 0.01

profits, buys, sales, take_profit_trades = \
    WR_strategy.wr_strategy(csv_data, dates, period, take_profit, bull_open, bull_close, starting_budget, stock_quantity, expenses)

x = np.arange(len(dates))

profit_fig, ax = plt.subplots(1, 1)
ax.plot(x, profits)
util.equidate_ax(profit_fig, ax, dates, fmt="%Y.%m.%d")
profit_fig.show()
#plt.close()

fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(25, 15))

ax1.plot(x, csv_data['Close'])
ax1.grid(True)
ax1.set_title('Close Price')
ax1.set_ylabel('Closing price')

ax1.plot(x[buys], csv_data['Close'][buys], 'r*')
ax1.plot(x[sales], csv_data['Close'][sales], 'g*')
ax1.plot(x[take_profit_trades], csv_data['Close'][take_profit_trades], 'k*')

ax2.plot(x, csv_data['%R'])
ax2.grid(True)
ax2.set_title('Williams %R')
ax2.set_ylabel('%R')

util.equidate_ax(fig, ax2, dates, fmt="%Y.%m.%d")

fig.show()

#plt.close()

# Optimization test
optimizationUtil.optimize_strategy(csv_data, dates, starting_budget, stock_quantity, expenses)


