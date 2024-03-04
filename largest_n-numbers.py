def find_larges_n_numbers(lt,n):
    list2 = sorted(lt,reverse=True)
    list3 = list2[:n]
    return list3

list1 = [i for i in range(101)]
#list1 = [10,22,334,111,21,4444,111,66,453,7866]
n = int(input("Enter a number"))

nlist = find_larges_n_numbers(list1,n)
print(nlist)