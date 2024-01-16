import random
num = int(input("Enter a number : "))
l1=[]
for i in range(1,num+1):
    l1.append(i)
print(l1)
print(random.choice(l1))