list1 = [1,2,3,4,5,6,7,2,3,111,2,33,44]
n = int(input("N = "))
count = 0
for i in list1:
    if i == n:
        count+=1
print(count)

list1 = [i for i in range(1,101) if i % 2 == 0]
print(list1)
print("Count == ", len(list1))

