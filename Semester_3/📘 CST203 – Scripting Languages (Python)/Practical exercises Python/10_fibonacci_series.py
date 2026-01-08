# 10. Fibonacci series

# Take input
n = int(input("Enter number of terms: "))

# First two numbers
a = 0
b = 1

print("Fibonacci series:")
print(a)

if n > 1:
    print(b)

# Print remaining numbers
i = 2
while i < n:
    c = a + b
    print(c)
    a = b
    b = c
    i = i + 1
