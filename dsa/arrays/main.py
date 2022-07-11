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

print('--------------------------------------------')

def traverse_array(arr):
    for i in arr:
        print(i, end=' ')


traverse_array(arr1)

print('\n--------------------------------------------')

def access_element(arr, idx): # O(1) time | O(1) space complexity
    if -len(arr) <= idx < len(arr):
        return arr[idx]

    return f"There is not any element in this index"


print(access_element(arr1, -10))


