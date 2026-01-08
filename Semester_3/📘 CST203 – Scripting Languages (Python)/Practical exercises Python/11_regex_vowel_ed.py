# 11. Words starting with vowels and ending with 'ed' using regex

import re

# Sample text
text = "animated arrived ended opened invited used created edited isolated educated"

# Find words starting with vowel and ending with ed
pattern = '[aeiou][a-z]*ed'

result = re.findall(pattern, text)

print("Words starting with vowel and ending with ed:")
for w in result:
    print(w)
