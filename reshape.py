# reshape(rows, coloumn) specify new shape
# if dimensions match

import numpy as np

arr = np.array([10,20,30,40,50,60])
reshaped_Arr = arr.reshape(2,3)  # (2,3) means 2X3 matrix
print(reshaped_Arr)
