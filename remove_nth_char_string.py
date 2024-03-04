str1 ="Data Scientist"
pos = 4
count = 0
for i in str1:
    if count == pos:
        i = ""
    else:
        print(i,end="")
    count+=1
print(" ")

str1 = "Hellow world"
i = 5
result = str1[:i] + str1[i+1:]
print(result)