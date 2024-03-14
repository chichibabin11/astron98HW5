#Given an array, output the array where all elements are equal
import numpy as np
arr = np.array([[1,1,1],[1,2,3],[2,2,2]])
equal_num = np.all(arr[:,:-1] == arr[:,1:], axis = 1) #why not axis=0?
result = arr[equal_num]
print (result)