n = 97
l1=[]
for i in range(1,27):
    l1.append(chr(n))
    n += 1
#    print(n)
print(l1)

for i in range(len(l1)):
#char = str(input("\n Enter the character : "))
    print(l1[i], ord(l1[i]))