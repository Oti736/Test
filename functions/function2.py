# Exercise 2: Flatten a nested list

def flatten_list(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))   # recursion
        else:
            flat.append(item)
    return flat

# Example
data = [1, [2, 3], [4, [5, 6]], 7,8,[9,10]]
print(flatten_list(data))   