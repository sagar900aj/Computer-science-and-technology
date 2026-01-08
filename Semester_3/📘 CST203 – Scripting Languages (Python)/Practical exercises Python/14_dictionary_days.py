# 14. Create dictionary of 7 days of a week

# Create dictionary
d = {}
d[1] = "Monday"
d[2] = "Tuesday"
d[3] = "Wednesday"
d[4] = "Thursday"
d[5] = "Friday"
d[6] = "Saturday"
d[7] = "Sunday"

# Print dictionary
print("Days of the week:")
print(d)
print()

# Print each day
for k in d:
    print(k, "-", d[k])
