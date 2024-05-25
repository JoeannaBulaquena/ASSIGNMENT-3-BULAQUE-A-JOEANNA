#SAVING AND WRITING FILES USING NUMPY

Example 1: Saving a Single Numpy Array as .npy File

import numpy as np

# Create a numpy array
array1 = np.array([1, 2, 3, 4, 5])

# Save the array as .npy file
np.save('array1.npy', array1)


Example 2: Saving Multiple Numpy Arrays as .npz File


import numpy as np

# Create multiple numpy arrays
array2 = np.array([6, 7, 8, 9, 10])
array3 = np.array([11, 12, 13, 14, 15])

# Save multiple arrays as .npz file
np.savez('arrays.npz', array2=array2, array3=array3)


Example 3: Saving Numpy Array as Text File


import numpy as np

# Create a 2D numpy array
array4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Save the array as text file
np.savetxt('array.txt', array4)


#LOAD DATA FROM FILES USING NUMPY

Example 1: Loading a Single Numpy Array from .npy File

import numpy as np

# Load a single array from .npy file
data1 = np.load('array1.npy')
print('Loaded Array from array1.npy:', data1)


Example 2: Loading Multiple Numpy Arrays from .npz File

import numpy as np

# Load multiple arrays from .npz file
data2 = np.load('arrays.npz')
array2 = data2['array2']
array3 = data2['array3']
print('Loaded Array 2 from arrays.npz:', array2)
print('Loaded Array 3 from arrays.npz:', array3)


Example 3: Loading Data from a Text File

import numpy as np

# Load data from text file
data3 = np.loadtxt('array.txt')
print('Loaded Data from array.txt:', data3)