import matplotlib.pyplot as plt
import pandas as pd


def calculate_williams_r(data, period):
    data['Highest'] = data['High'].rolling(period).max()
    data['Lowest'] = data['Low'].rolling(period).min()
    filtering_condition = (data['Highest'] != 0) & (data['Lowest'] != 0)
    data.loc[filtering_condition, '%R'] = (data['Highest'] - data['Close']) / (data['Highest'] - data['Lowest']) * -100
    return data


def williams_r(file_name='../resource/HistoricalData_apple.csv',
               start_date='06/11/2020',
               end_date='03/12/2021',
               figure_title='Will %R',
               period=14):
    date_format = "%Y.%m.%d"
    data = pd.read_csv(file_name)
    data['Time'] = pd.to_datetime(data['Time'], format=date_format)
    data = data.set_index('Time')
    data = data.iloc[::-1]

    data = calculate_williams_r(data, period)

    subplot_data_close = data['Close'].loc[start_date:end_date]
    subplot_data_william_r = data['%R'].loc[start_date:end_date]

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex='col')
    ax1.set_title(figure_title)
    subplot_data_william_r.plot(ax=ax2)
    subplot_data_close.plot(ax=ax1)
    ax1.grid()
    ax2.grid()
    plt.xticks(rotation=45)
    fig.subplots_adjust(hspace=0.0)
    fig.show()


williams_r()
