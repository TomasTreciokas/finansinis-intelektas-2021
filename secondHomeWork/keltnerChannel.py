import matplotlib.pyplot as plt
import pandas as pd


def get_tr_calculation_parameters(data):
    data['H-L'] = data['High'] - data['Low']
    data['H-C.1'] = 0
    data['C.1-L'] = 0
    for i in range(1, len(data.index)):
        previous_close = data.iloc[i - 1, data.columns.get_loc('Close')]
        today_high = data.iloc[i, data.columns.get_loc('High')]
        today_low = data.iloc[i, data.columns.get_loc('Low')]

        data.iloc[i, data.columns.get_loc('H-C.1')] = abs(today_high - previous_close)
        data.iloc[i, data.columns.get_loc('C.1-L')] = abs(previous_close - today_low)
    return data


def true_range(data):
    data['TR'] = 0
    for i in range(len(data.index)):
        high_low = data.iloc[i, data.columns.get_loc('H-L')]
        high_pr_close = data.iloc[i, data.columns.get_loc('H-C.1')]
        pr_close_low = data.iloc[i, data.columns.get_loc('C.1-L')]
        data.iloc[i, data.columns.get_loc('TR')] = max(high_low, high_pr_close, pr_close_low)
    return data


def average_true_range(data, period):
    data['ATR'] = 0
    data = true_range(get_tr_calculation_parameters(data))

    data.iloc[period-1, data.columns.get_loc('ATR')] = data['TR'].head(period).mean()
    for i in range(period, len(data.index)):
        current_tr = data.iloc[i, data.columns.get_loc('TR')]
        pr_atr = data.iloc[i - 1, data.columns.get_loc('ATR')]
        data.iloc[i, data.columns.get_loc('ATR')] = ((pr_atr * (period-1)) + current_tr) / period

    return data['ATR']


def exponential_moving_average(data, period):
    data_frame = data.to_frame()
    data_frame['EMA'] = 0

    data_frame.iloc[period - 1, data_frame.columns.get_loc('EMA')] = data.head(period).mean()
    multiplier = (2 / (period + 1))
    print(data_frame.head(2))
    for i in range(period, len(data_frame.index)):
        previous_ema = data_frame.iloc[i - 1, data_frame.columns.get_loc('EMA')]
        current_price = data_frame.iloc[i, data_frame.columns.get_loc('Close')]
        data_frame.iloc[i, data_frame.columns.get_loc('EMA')] = (current_price - previous_ema) * multiplier + previous_ema

    return data_frame['EMA']


def keltner_channel(file_name='../resource/HistoricalData_apple.csv',
                    start_date='06/11/2020',
                    end_date='03/12/2021',
                    figure_title='Keltner channel',
                    period=20):
    data = pd.read_csv(file_name)
    data['Time'] = pd.to_datetime(data['Time'], format="%Y.%m.%d")
    data = data.set_index('Time')
    data = data.iloc[::-1]

    data['Middle/EMA'] = exponential_moving_average(data['Close'], period)
    data['ATR'] = average_true_range(data, period)
    data['Upper'] = data['Middle/EMA'] + (data['ATR'])
    data['Lower'] = data['Middle/EMA'] - (data['ATR'])

    plot_data = data[['Middle/EMA', 'Upper', 'Lower', 'Close']].loc[start_date:end_date]
    plt.plot(plot_data)
    plt.title(figure_title)
    plt.legend(['Middle/EMA', 'Upper', 'Lower', 'Close'])
    plt.ylabel('Close')
    plt.xlabel('Time')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()


keltner_channel()
