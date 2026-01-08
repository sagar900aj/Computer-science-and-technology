# 13. Copy contents of one file to another

# Take input
source = input("Enter source file name: ")
dest = input("Enter destination file name: ")

# Open and read source file
f1 = open(source, 'r')
data = f1.read()
f1.close()

# Open and write to destination file
f2 = open(dest, 'w')
f2.write(data)
f2.close()

print("File copied")
