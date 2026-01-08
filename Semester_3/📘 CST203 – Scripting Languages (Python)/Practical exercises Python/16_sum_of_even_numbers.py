# 16. Sum of even numbers in a list

# Create a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("List:")
print(numbers)

# Find sum of even numbers
s = 0
for n in numbers:
    if n % 2 == 0:
        s = s + n

print("Sum of even numbers:")
print(s)
