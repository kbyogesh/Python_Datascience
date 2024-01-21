n1 = 10
n2 = 1000

for num in range(n1,n2+1):
    order = len(str(num))
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    
    if sum == num:
        print(num)