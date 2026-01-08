# 5. Retrieve strings starting with 'm' and having 5 characters

# List of strings
words = ["mango", "apple", "melon", "match", "mouse", "mat", "music", "metro"]

print("Words starting with m and having 5 characters:")

# Check each word
for w in words:
    count = 0
    for c in w:
        count = count + 1
    
    if w[0] == 'm' and count == 5:
        print(w)
