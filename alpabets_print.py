#program to display the alphabets based on its ascii value

for i in range(64,123):
    if i >= 65 and i <= 90:
        print(chr(i),end=" ")
        if(chr(i) == "Z"):
            print("")

    elif i > 96 and i <= 122:
        print(chr(i),end=" ")
        if(chr(i) == "z"):
            print("")
