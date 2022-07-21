# -*- coding: utf-8 -*-
from array import *

arr_int = array('i', [3, -1, 4, 5, 100, 67, 89])

for x in arr_int: # time O(N) - space O(1)
    print(x)

print("Step 2 - Append")
print(arr_int[0]) # 3
print(arr_int[3]) # 5

print("Step 3")
arr_int.append(1000)
print(arr_int)

print("Step 4 - Insert")
arr_int.insert(0, 12)
arr_int.insert(3, 13)
print(arr_int)

print("Step 5 - Extend")
print(arr_int)
temp = array('i', [3, 4, 5, 6])

arr_int.extend(temp)
print(arr_int)

print("Step 6 - fromlist()")
temp_lst = [20, 21, 22]
arr_int.fromlist(temp_lst)
print(arr_int)

print("Step 7 - Remove") # O(N)
arr_int.remove(3)

print(arr_int)

print("Step 8 - Pop remove last element")
elem = arr_int.pop()
print(elem)
print(arr_int)
