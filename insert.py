# np.insert(array, index, value asix=None)
# array - original array
# index - place where to insert
# value - no kya dalna h vo 
# axis - 0 means we have to insert it in row-wise 
# axis - 1 means we have to insert it in column-wise 


import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr,2,100)
print(new_arr)