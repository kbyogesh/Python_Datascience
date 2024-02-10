def cube_of_sum(n):
    sum1 = 0
    if n == 0:
        return 0
    else:
        for i in range(1,n+1):
            sum1 = sum1 + (i ** 3)
        return sum1

num = int(input("Enter value: "))
if num < 0:
    print("Enter postitive value ")
else:
    sum_add = cube_of_sum(num)
    print(sum_add)