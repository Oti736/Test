# Program 4: Remove all occurrences of 20 from the list
lst = [5, 20, 15, 20, 25, 50, 20]

result = [x for x in lst if x != 20]

print("Original list:", lst)
print("List after removing all 20s:", result)
