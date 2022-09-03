listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

listAinB = [x for x in listA if x in listB]
print(listAinB)

listBinA = [x for x in listB if x in listA]
print(listBinA)

listAinB = list(filter(lambda x: x in listB, listA))
print(listAinB)

listBinA = list(filter(lambda x: x in listA, listB))
print(listBinA)
