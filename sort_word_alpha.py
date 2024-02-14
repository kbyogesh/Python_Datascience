mystr = input("Enter a string")
mystr1 = []
for text in mystr.split():
    #mystr1 = text
    mystr1.append(text)

mystr1.sort()

print(mystr1)
