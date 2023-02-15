import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout': True})

df = pd.read_csv('flight_delays.csv')

d = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Month').Month.count()
d = d.reset_index(name='count')
c = [0]*4
for index, row in d.iterrows():
    m = int(row['Month'].replace('c-', ''))
    if m in (12, 1, 2):
        c[0] += row['count']
    elif m in range(3,6):
        c[1] += row['count']
    elif m in range(6,9):
        c[2] += row['count']
    else:
        c[3] += row['count']
t = pd.DataFrame({
    'Время года': ['зима', 'весна', 'лето', 'осень'],
    'Количество задержек': c
    })
ax = t.plot(x='Время года', y='Количество задержек', kind='bar')
ax.figure.savefig('4.png')
