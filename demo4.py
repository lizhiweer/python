msg = input("请输入些什么:")

print(msg)

file = open("testFile.txt", "w")
print(msg, file=file)
file.close()
