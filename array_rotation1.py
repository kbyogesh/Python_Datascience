arr = [7,9,10,1,2,3]
k = 3
n = len(arr)
arr1=[0]*n
for i in range(n):
    arr1[i] = arr[(i+k) % n]
print(arr1)

arr2 = arr[:k]
arr3 = arr[k:]
arr4 = arr2 + arr3
print(arr4)