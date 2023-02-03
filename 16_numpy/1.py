import numpy as np


# 1
a = np.arange(12, 43)
print(a)

# 2
a = np.zeros((12,))
a[4] = 1
print(a)

# 3
a = np.arange(0, 9)
b = a.reshape((3, 3))
print(b)

# 4
a = np.array([1,2,0,0,4,0])
print(a[a > 0])

# 5
a = np.ones((5, 3))
b = np.ones((3, 2))
print(a.dot(b))

# 6
a = np.ones((8, 8)) 
o = np.zeros((1,8))
print(o)
a = np.vstack((o, np.vstack((a, o))))
o = np.zeros((10,1))
a = np.hstack((o, np.hstack((a, o))))
print(a)

# 7
a = np.random.random((10,))
print(sorted(a))

# 8
# np.ndenumerate()

# 9
a = np.random.random((16,))
b = a.reshape((4,4))
e = np.sum(b, axis=0) / 4
b_sq = b**2
e_sq = np.sum(b_sq, axis=0) / 4
d = e_sq - e**2
print((b-e)/d**0.5)

# 10
a = np.arange(5,10)
idx = (np.abs(a-10)).argmin()
print(a[idx])

# 11
a = np.random.random((10,))
a.sort()
N = 5
print(a[10-N:10])
