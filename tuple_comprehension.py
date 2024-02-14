my_tuple = (i for i in range(1, 10))
print(my_tuple)
# <generator object <genexpr> at 0x7fb91b151430>
for i in my_tuple:
    print(i,end=", ")

my_dict = {i for i in range(1, 10)}
print(my_dict)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_list = [i for i in range(1, 10)]
print(my_list)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}