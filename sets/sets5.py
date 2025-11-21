# Exercise 5: Count vowels in a string

text = "Understanding sets is easy."
vowels = "aeiouAEIOU"

count = sum(1 for char in text if char in vowels)

print("The given string has", count, "vowels.")
