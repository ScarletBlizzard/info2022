import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})

df = pd.read_csv('flight_delays.csv')

n = df.groupby('Origin').Dest.count()
y = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Origin').Dest.count()
tf = y / n
tf = tf.reset_index(name='Частота задержек') \
    .sort_values('Частота задержек', ascending=False).head(10)
ax = tf.plot(x='Origin', y='Частота задержек', kind='bar')
plt.xlabel('Аэропорт')
ax.figure.savefig('6.png')
