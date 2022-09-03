lst = list({
    tuple(sorted({x, y, z}))
    for x in range(1, 101)
    for y in range(1, 101)
    for z in range(1, 101)
    if x**2 + y**2 == z**2
})

print(len(lst))
print(lst)
