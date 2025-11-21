# Program 3: Replace first occurrence of 20 with 200
lst = [5, 10, 15, 20, 25, 50, 20]

if 20 in lst:
    index = lst.index(20)
    lst[index] = 200

print("Updated list:", lst)
