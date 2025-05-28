import numpy as np

vec1 = np.array([1., 3., 5.])
print(vec1 * 2)
print(vec1 * vec1)
print(vec1 / 2)
print(vec1 + vec1)

vec2 = np.array([2., 4.])
try:
    print(vec1 + vec2)
except ValueError as e:
    print(e)

vec3 = np.array([2., 4., 6.])
print(vec1 + vec3)
print(vec1 / vec3)
print(vec1 * vec3)
print(2 * vec1 + 5 * vec3)