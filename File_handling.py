f = open("file.txt", "w+")

f.write("Hello, World!\n")
f.write("This is a test file.\n")
f.seek(0)
Data=f.read()
print(Data)
f.close()