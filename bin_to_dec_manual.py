n = 11011
sum = 0
count = 0
d = n % 10
if d == 0:
    sum = 0
else:
    sum = 1
n = n // 10
count += 1
while n > 0:
    d = n % 10 
    print(sum,count)
    sum = sum + (d * (2 ** count))
    n = n // 10
    count += 1
print(sum)

