# 15. Factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Take input
num = int(input("Enter a number: "))

# Calculate and display
result = factorial(num)
print("Factorial of", num, "is", result)
