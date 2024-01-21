# To find the number is Armstrong 
num = int(input("Enter a number :"))

num_len = len(str(num))
sum = 0
temp = num
if num <=0:
    print("Enter positive number")
else:
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_len
        temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("not an Armstrong number")