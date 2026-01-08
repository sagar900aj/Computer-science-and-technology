# 9. Return the rightmost digit

def rightmost_digit(num):
    digit = num % 10
    return digit

# Take input
number = int(input("Enter a number: "))

# Get rightmost digit
result = rightmost_digit(number)

print("Rightmost digit is:", result)
