def mono(arr):
    n = len(arr)
    if n == 1:
        return True
    elif all(arr[i]>=arr[i-1] for i in range(1,n)):
        return True
    elif all(arr[i]<=arr[i-1] for i in range(1,n)):
        return True
    else:
        return False


arr1 = [1,2,3,4,5]
arr2 = [1,2,5,4,3,1]
arr3 = [5,4,3,2,2,1]
arr4 = [10,10,5,4,2,2,1]

print("arr1 :",mono(arr1))
print("arr2 :",mono(arr2))
print("arr3 :",mono(arr3))
print("arr4 :",mono(arr4))