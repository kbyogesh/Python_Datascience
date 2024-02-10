num = 125
count=len(str(num))
#a = sum(int(i)**(index+i) for index, i in enumerate(num,1))
#print(a)

tmp = num
sum = 0

#count=num_str
print(count)
while tmp > 0:
    digit = tmp % 10
    sum = sum + (digit ** count)
    print(digit)
    tmp = tmp // 10
    count-=1
print(sum)



