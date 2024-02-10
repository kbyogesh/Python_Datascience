d = 3
arr = [1,2,3,4,5]
n = len(arr)
arr1 = [0]*n
for i in range(n):
    arr1[i] = arr[(i+d) % n]
    print((i+d)%n)

print(arr1)