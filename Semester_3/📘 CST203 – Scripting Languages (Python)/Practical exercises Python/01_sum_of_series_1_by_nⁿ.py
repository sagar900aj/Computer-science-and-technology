# 1. Write a Python program to print the sum of the series:
#    **1 + 1/2² + 1/3³ + …… + 1/nⁿ**

n = int(input("Enter a number : "))
result = 0
for x in range(1, n + 1):
    sum = 1 / (x ** x)
    result = result + sum 
print("Sum of the series =",result) 