# Program 2: Remove empty strings from the list
lst = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Filter out empty strings
result = [x for x in lst if x != ""]

print("Original list:", lst)
print("After removing empty strings:", result)
