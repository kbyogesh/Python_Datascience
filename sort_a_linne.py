str1 = str(input("Enter a string"))
word = [word.capitalize() for word in str1.split()]
word.sort()
for text in word:
    print(text)