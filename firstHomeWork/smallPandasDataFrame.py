import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

dates = pd.date_range('20190214', periods=6)
numbers = np.array([[101, 103], [105.5, 75], [102, 80.3], [100, 85], [110, 98], [109.6, 125.7]])
df = pd.DataFrame(numbers, index=dates, columns=['A', 'B'])

# 1.
print(df.loc['2019-02-18'])
# 2.
df.loc[np.datetime64(datetime.datetime(2019, 2, 18))]
# 3.
df.tail(2).head(1)
# 4.
df.head(2)['B']
# 5.
df.sort_values('B', ascending=False)
# 6.
df.max()['A']
# 7.
df.iloc[df['A'].argmax()]['A'] = df['A'].max() * 2
# 8.
df[df['A'] > 105]
# 9.
plt.plot(df['A'])
plt.show()
# 10.
df = df[df['A'] >= df['B']]
