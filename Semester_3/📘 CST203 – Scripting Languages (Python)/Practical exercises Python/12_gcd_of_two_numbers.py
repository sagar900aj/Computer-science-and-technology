# 12. Find GCD of two numbers

# Take input
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))

# Find GCD using Euclidean algorithm
while n != 0:
    temp = n
    n = m % n
    m = temp

print("GCD is:", m)
