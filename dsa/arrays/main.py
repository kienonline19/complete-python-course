from array import *

# Create arrays
# O(1)
# other langs => O(N)
arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.5, 2, 3, 4, 5])

# Insertion
arr1.insert(6, 7)
print(arr1)

arr1.insert(0, 0)
print(arr1)

arr1.insert(2, -1)
print(arr1)
