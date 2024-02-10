num = 19
sum = 0

while True:
    while num > 0:
        tmp = num
        digit = tmp % 10
        sum = sum + (digit ** 2)
        num = tmp//10
        print(tmp,sum)
    if sum == 1:
        print("Happy Number")
        break
    else:
        num = sum
        #continue
