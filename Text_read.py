read_file = open("Text_write.txt","r")
print(read_file.read())
#read_file.close()
read_file.seek(0)
print("Bytes -------")
print(read_file.read(10))
print("-----END Bytes -------")

print()

file1 = open("Text_write1.txt","w")
file1.write("Hi From python TEXT_READ file\n")
file1.close()

file2 = open("Text_write1.txt","a")
file2.write("appending the text\n")
#file2.close()

file2 = open("Text_write1.txt","r")
print(file2.read())
