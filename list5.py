# Program 5: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ri"]
list2 = ["y", "me", "s", "ck"]

result = [a + b for a, b in zip(list1, list2)]

print("List 1:", list1)
print("List 2:", list2)
print("Concatenated list:", result)
