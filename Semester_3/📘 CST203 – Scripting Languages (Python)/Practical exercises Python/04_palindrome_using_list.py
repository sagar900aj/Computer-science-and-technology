# 4. Check whether a string is palindrome using list

# Take input
s = input("Enter a string: ")

# Convert string to list
l = []
for c in s:
    l.append(c)

# Reverse the list manually
r = []
for i in range(len(l) - 1, -1, -1):
    r.append(l[i])

# Check if same
flag = 1
for i in range(len(l)):
    if l[i] != r[i]:
        flag = 0
        break

if flag == 1:
    print("Palindrome")
else:
    print("Not palindrome")
