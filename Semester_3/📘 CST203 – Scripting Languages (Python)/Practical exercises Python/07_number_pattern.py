# 7. Print pattern: 1, 121, 12321

n = 3

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print ascending numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # Print descending numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()
