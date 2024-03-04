def find_words(ls1,n):
    list1 = []
    for i in ls1:
        if len(i) > n:
            list1.append(i)
    return list1

list2 = ['apple','bannana','lime','mangoes','melon','water melon']
k = 5
list3 = find_words(list2,5)
print(list3)






