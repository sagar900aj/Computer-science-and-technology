# 8. Count vowels, consonants, and digits in a string

# Take input
string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0

for char in string:
    if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
        # It's a letter
        if char in "aeiouAEIOU":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    elif char >= '0' and char <= '9':
        # It's a digit
        digits = digits + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
