lst1 = [1, 2, 3, 4, 5]
lst2 = lst1

lst2[0] = 10

print(lst1)


slc1 = [3, 4, 5, 6]
slc2 = slc1[:2]

slc2[0] = 30

print(slc1)

print(slc1, slc2)