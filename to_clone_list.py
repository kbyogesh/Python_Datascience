list1 = [1,2,3,4,5,6]
list2 = list1[:]
print(list2)

list2 = list(list1)
print(list2)

list2 = [i for i in list1]
print(list2)
