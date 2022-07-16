from array import *

arr_int = array('i', [3, -1, 4, 5, 100, 67, 89])

for x in arr_int: # time O(N) - space O(1)
    print(x)

print("Step two")
print(arr_int[0]) # 3

print(arr_int[3]) # 5
