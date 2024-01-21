num = int(input("Enter a number: \n"))
Fact = 1
if num < 0:
    print(f"{num} is negative number")
elif num == 0:
    print(f"Factorial of {num} is {Fact}")
else:
    for i in range(1,num+1):
        Fact = Fact * i
    print(f"Factorial of {num} = {Fact}")
