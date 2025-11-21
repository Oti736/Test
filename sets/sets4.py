# Exercise 4: Check if two sets intersect

given_a = {10, 20, 30, 40, 50,60}
given_b = {60, 70, 80, 90, 10,60}

common = given_a.intersection(given_b)

if common:
    print("The two sets have items in common:")
    print(common)
else:
    print("No common items found.")
