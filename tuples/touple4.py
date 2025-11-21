# Exercise 4: Pair combinations of two tuples

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")

pairs = [(x, y) for x in tuple1 for y in tuple2]

print("All pair combinations:")
for pair in pairs:
    print(pair)
