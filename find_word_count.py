str1 = "This is a text and it is used to read myfile".split()
print(str1)
str2="is"
#str3=str1.split()
count = 0
for char in str1:
    if str2 == char:
        count+=1
print(count)
