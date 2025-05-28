import numpy as np

v = np.array([1., 2., 3., 4., 5.])
print(np.sum(v))
print(v.shape)
print(v.transpose())
v1 = v[:2]
print(v1)
v[0] = 5
print(v)
print(v1)
try:
    v1[:2] = [1., 2., 3.]
except ValueError as e:
    print(e)
v1[:2] = [1., 2.]
print(v)
v3 = 2 * v[:2] + v1 * 3
print(v3)
v1 = [4, 6]
print(v3)
print(v)
print(v + 10.0)
print(np.sqrt(v))
print(np.cos(v))
print(np.sin(v))
v1_dot = np.array([1., 2.])
v3_dot = np.array([4., 5.])
print(np.dot(v1_dot, v3_dot))
print(v1_dot.dot(v3_dot))
print(v3_dot.dot(v1_dot))