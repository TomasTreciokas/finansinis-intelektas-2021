import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

index = pd.date_range('2020-3-1', periods=1000, freq='B')
data = (np.random.random((1000, 1))-0.5).cumsum(axis=0)
df = pd.DataFrame(data, index=index, columns=['kaina'])
print(df)
df.plot()
plt.grid()
plt.show()
# add grid