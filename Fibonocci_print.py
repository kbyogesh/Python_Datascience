num = int(input("Enter number of terms \t:"))
first = 0
second = 1
count = 0
if num < 0:
    print("Negative number")
elif num == 1:
    print(first)
else:
    while count < num:
        print(first, end=" ")
        next = first + second
        first = second
        second = next
        count+=1
print("")