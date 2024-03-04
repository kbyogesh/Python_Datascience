str1 = "Hello world"
str2 = ""
for i in str1:
    str2 =i + str2
    
print(str2)

list1 = [1,2,3,4]
list1.clear()
#list1 = [ ]
#list1 =""
for i in range(len(list1)):
    list1[i] = i
print(len(list1))
print(list1)

arr1 = [2,3,1,4]
arr2 = arr1[::-1]
print(arr2)

str2 = "Hai"
str1 = str2[::-1]
print(str1)