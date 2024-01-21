n = 27
l1 = []
rem = 0
while n > 0:
    x = n % 2
    rem = l1.append(x)
    n = n // 2
print(l1[::-1])
print(len(l1))
for i in range(len(l1)-1,-1,-1):
    print(l1[i],end="")