lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]

lst1.extend(lst2)

print(lst1) # [1, 2, 3, 4, 5, 6, 7, 8]

# extend nhận bất cứ iterables nào còn + phải cùng kiểu
print(lst1 + lst2)

# TypeError: only list to list not tuple
# print([1, 2, 3] + (4, 5, 6))

tup3 = (5, 5, 6, 7)
lst1.extend(tup3) # [1, 2, 3, 4, 5, 6, 7, 8, 5, 5, 6, 7]
print(lst1)
