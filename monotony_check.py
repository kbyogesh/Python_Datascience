arr = [1,2,3,4,5]
arr1 = [5,4,3,1]
arr2 = [1,1,6,4,5]

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        if len(arr):
            print("Ascending")
            break
    elif arr[i] < arr[i-1]:
        if len(arr):
            print("Descending")
            break
    else:
        if (arr[i] > arr[i-1] or arr[i] < arr[i-1] for i in range(len(arr))):
                print("Not Monotony")
                break



def ismonotony(arr):
    increasing = decreasing = True

    for i in range(1,len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False

        elif arr[i] < arr[i - 1]:
            increasing = False
        
    return increasing or decreasing

arr = [1,2,3,3,4]
arr1 = [4,3,2,1]
arr2 = [3,1,4,2]

print("Array 1 :", ismonotony(arr))
print("Array 2 :", ismonotony(arr1))
print("Array 3 :", ismonotony(arr2))

