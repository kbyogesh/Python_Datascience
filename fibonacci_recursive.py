def fibo(n):
    if n <= 1:
        print(n)
    else:
        return(fibo(n-1)+fibo(n-2))

num = int(input("Enter number greater than 0"))

if num <= 0:
    print("Enter positive value")
else:
    for i in range(num):
        print(fibo(i),end=" ")