# Exercise 3: Find repeated items in a tuple

my_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 2)

repeated = set([item for item in my_tuple if my_tuple.count(item) > 1])

print("Repeated items:", repeated)
