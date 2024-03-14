#8x8 matrix with alternating 0 and 1
import numpy as np

arr = np.zeros((8,8), dtype = int)
arr[::2,::2] = 1
arr[1::2,1::2] = 1
print (arr)