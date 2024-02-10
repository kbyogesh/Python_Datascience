arr = [10,2,33,22,1,3,11]

for x in range(len(arr)-1):
    if arr[x] > arr[x+1]:
        arr[x], arr[x+1] = arr[x+1], arr[x]

print(arr)

arr = [10,2,33,22,1,3,11]

n = len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)