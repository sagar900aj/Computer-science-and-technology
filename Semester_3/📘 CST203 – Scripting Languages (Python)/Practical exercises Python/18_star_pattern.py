# 18. Print a pattern

# Take input
n = int(input("Enter number of rows: "))

# Print pattern
i = 1
while i <= n:
    # Print spaces
    j = 1
    while j <= n - i:
        print(" ", end="")
        j = j + 1
    
    # Print stars
    k = 1
    while k <= 2 * i - 1:
        print("*", end="")
        k = k + 1
    
    print()
    i = i + 1
