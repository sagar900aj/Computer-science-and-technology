# 2. Create a tuple of 5 digits and insert a new digit

# Create tuple with 5 digits
t = (1, 2, 3, 4, 5)
print("Original tuple:")
print(t)

# Take input
num = int(input("Enter digit to insert: "))
pos = int(input("Enter position: "))

# Convert tuple to list
l = []
for i in t:
    l.append(i)

# Insert digit
l.insert(pos, num)

# Convert list to tuple
new_t = ()
for i in l:
    new_t = new_t + (i,)

print("New tuple:")
print(new_t)
