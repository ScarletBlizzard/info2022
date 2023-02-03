import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 16, 100)

def f(u):
    return np.sin(u/5)*np.exp(u/10)+5*np.exp(-u/2) 

y = f(x)

A = np.array(
        [[1, 1,  1,     1    ],
         [1, 4,  4**2,  4**3 ],
         [1, 10, 100,   1000 ],
         [1, 15, 15**2, 15**3]])
b = np.array([f(1), f(4), f(10), f(15)])

w0, w1, w2, w3 = np.linalg.solve(A, b)
P = w0 + w1*x + w2*x**2 + w3*x**3
print(w0, w1, w2, w3)

fig = plt.figure()
plt.plot(x, y)
plt.plot(x, P, "r")
plt.savefig("3_plot.png")

