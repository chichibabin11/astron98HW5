import numpy as np

np.random.seed(12345)
arr = np.random.randint(1,50, (4,5))
sort = np.sort(arr, axis = 0)
print (sort)