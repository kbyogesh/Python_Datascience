list1 = [222,444,1,2223,4443,23,11,10,899,14]

list2 = [num for num in list1 if num % 2 == 0]

print(list2)

list2 = [num for num in list1 if num % 2 != 0]

print(sorted(list2))