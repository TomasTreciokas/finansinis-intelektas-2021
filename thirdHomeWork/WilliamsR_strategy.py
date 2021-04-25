import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import secondHomeWork.willR as will_r


def wr_strategy(csv_data, dates, period, take_profit, bull_start_bound, bull_end_bound, initial_budget, stock_quantity, expenses):
    william_r_data = will_r.calculate_williams_r(csv_data, period)
    william_r_data = william_r_data[['Close', '%R']]

    profits = pd.Series(np.zeros(len(william_r_data)))
    profits[0] = initial_budget
    buys = pd.Series(np.full(len(william_r_data), False), index=dates)
    sales = pd.Series(np.full(len(william_r_data), False), index=dates)
    profit_trades = pd.Series(np.full(len(william_r_data), False), index=dates)

    bull_take_profit = 0
    bull_trend = False
    buy_index = 0

    for i in range(period, len(william_r_data)):
        current_close_price = william_r_data['Close'][i]
        current_williamr = william_r_data['%R'][i]
        if not bull_trend:
            bull_trend_start_signal = (current_williamr > bull_start_bound)
            if bull_trend_start_signal:
                bull_trend = True
                buy_index = i
        if bull_trend:
            bull_trend_end_signal = (current_williamr < bull_end_bound)
            if i == buy_index:
                if bull_trend_end_signal:
                    bull_trend = False
                else:
                    bull_take_profit = current_close_price + take_profit
            elif bull_trend_end_signal and i > buy_index:
                bull_trend = False
                buys.iat[buy_index] = True
                sales.iat[i] = True
                trade_value = (current_close_price - william_r_data['Close'][buy_index]) * stock_quantity - expenses
                profits[i] = trade_value
            elif current_close_price >= bull_take_profit and i > buy_index:
                bull_trend = False
                buys.iat[buy_index] = True
                profit_trades[i] = True
                trade_value = (current_close_price - william_r_data['Close'][buy_index]) * stock_quantity - expenses
                profits[i] = trade_value

    profits = profits.cumsum()

    return profits, buys, sales, profit_trades


def optimize_strategy(data_pd, dates, starting_budget, stock_quantity, trade_expenses):
    df_opt = pd.DataFrame(columns=['opt_period', 'sharpe_ratio', 'rez'])
    for opt_period in range(1, 252):
        profits, buys, sales, profit_trades = wr_strategy(data_pd, dates, opt_period, 10, -50, -20, starting_budget, stock_quantity, trade_expenses)
        sharpe_ratio = annualised_sharpe(pd.Series(profits.cumsum()))
        df_opt = df_opt.append({'opt_period': opt_period, 'sharpe_ratio': sharpe_ratio, 'rez': profits.copy()}, ignore_index=True)

    idx_max = df_opt['sharpe_ratio'].idxmax()
    optimal_period = df_opt.loc[idx_max]['opt_period']
    print('Didziausias sarpo santykis ({}) yra su parametrais opt_period: {}'.format(df_opt.loc[idx_max]['sharpe_ratio'], optimal_period))

    profits, buys, sales, profit_trades = wr_strategy(data_pd, dates, optimal_period, 10, -50, -20, starting_budget, stock_quantity, trade_expenses)
    df = pd.DataFrame(profits, columns=['Profit'])
    df.plot()
    plt.grid()
    plt.show()


def annualised_sharpe(returns, n=252):
    r = (returns - returns.shift(1))/returns.shift(1)
    return (r.mean() * n) / (r.std() * np.sqrt(n))
