# slicing 

# array[start:stop:step]

# arr[start:end] , start to end -1


import numpy as np

arr = np.array([10,20,30,40,50])
print(arr[0:4])   # n-1 rhega hamesha
print(arr[:4])  # index 0 to 3
print(arr[::2]) # picks every second element
print(arr[::-1]) # reverse full
