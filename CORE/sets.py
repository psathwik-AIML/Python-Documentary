# Set = No duplicates, Unordered, Mutable

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))         # {1, 2, 3, 4, 5}
print(s1.intersection(s2))  # {3}
# make set empty
s1.clear()
print(s1)