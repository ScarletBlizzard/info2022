import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.subplots_adjust(bottom=0.15)

df = pd.read_csv('flight_delays.csv')

n = df.groupby('Month').Dest.count()
y = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Month').Dest.count()
tf = y / n
ax = tf.plot(x='Month', y='count', kind='bar')
plt.xlabel('Месяц')
plt.ylabel('Доля задержек')
ax.figure.savefig('1.png')
