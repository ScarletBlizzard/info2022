import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.subplots_adjust(bottom=0.15)

df = pd.read_csv('flight_delays.csv')

d = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Distance').Dest.count()
ax = d.plot(x='Distance', y='count', style='.')
plt.xlabel('Длина пути')
plt.ylabel('Количество задержек')
ax.figure.savefig('2.png')
