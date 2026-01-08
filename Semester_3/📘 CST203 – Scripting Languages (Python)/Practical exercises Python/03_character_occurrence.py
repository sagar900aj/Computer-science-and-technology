# 3. Count number of occurrences of a character in a string

# Take input from user
string = input("Enter a string: ")
char = input("Enter character to count: ")

# Count occurrences
count = 0
for c in string:
    if c == char:
        count = count + 1

print("Character", char, "appears", count, "times")
