from array import *

arr_int = array('i', [3, -1, 4, 5, 100, 67, 89])

for x in arr_int: # time O(N) - space O(1)
    print(x)

print("Step 2")
print(arr_int[0]) # 3
print(arr_int[3]) # 5

print("Step 3")
arr_int.append(1000)
print(arr_int)
