import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})

df = pd.read_csv('flight_delays.csv')

n = df.groupby('Dest').Dest.count()
y = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Dest').Dest.count()
t = y / n
t = t.reset_index(name='Частота задержек').sort_values('Частота задержек', ascending=False).head(5)
ax = t.plot(x='Dest', y='Частота задержек', kind='bar')
plt.xlabel('Направление')
ax.figure.savefig('3.png')
