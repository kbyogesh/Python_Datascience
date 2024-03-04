n = int(input("Enter a number"))
prime = False
for i in range(2,n):
    if n % i == 0:
        prime = True
        break
if prime:
    print("Not a prime number")
else:
    print("Prime")
