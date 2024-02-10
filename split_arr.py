arr = [1,2,3,4,5,6,7,8,9,10]
position = 5
n = len(arr)
arr1 = [0] * (position)
arr2 = [0] * (n - (position))
#print(n,position)
i = 0
for j in range(n):
    #print(j)
    if j < position:
        arr1[j] = arr[j]
        #print("if",arr1)
    else:
        arr2[i] = arr[j]
        i+=1
        #print("else",arr2)
merge_arr = arr2 + arr1
print(arr)
print(merge_arr)


arr = [11,22,33,55,44,33,77,99]
k = 3
firarr = arr[k::]
secarr = arr[::k]
print(secarr)

mergearr = firarr + secarr
print(mergearr)