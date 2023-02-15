import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})

df = pd.read_csv('flight_delays.csv')

d = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('DayOfWeek').Dest.count()
ax = d.plot(x='DayOfWeek', y='count', kind='bar')
plt.xlabel('День недели')
plt.ylabel('Количество задержек')
ax.figure.savefig('7.png')
