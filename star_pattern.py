n=5;i=0
while(i<=n):
    print(" " * (n - i) +"*" * i) 
    i+=1
print()

print("---------------")
n = 5
k = n - 1
for i in range(n):
    for j in range(k):
        print(end=" ")
    k = k - 1
    for j in range(i+1):
        print("* ",end="")
    print("\r")