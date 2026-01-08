# 17. Sum of series: x - x²/2 + x³/3 - x⁴/4 … (-1)ⁿ⁻¹(xⁿ)/n

# Take input
x = float(input("Enter x: "))
n = int(input("Enter n: "))

# Calculate sum
s = 0
for i in range(1, n + 1):
    power = 1
    for j in range(i):
        power = power * x
    
    term = power / i
    
    if i % 2 == 0:
        s = s - term
    else:
        s = s + term

print("Sum:")
print(s)
