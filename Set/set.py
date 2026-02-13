my_set = {"a","b","c","c","e","y"}
print("set:", my_set)

# add
my_set.add("g")
print("after add:", my_set)

# remove
my_set.remove("b")
print("after remove:", my_set)

# update
new_set = {"x","y","z","g","c"}
my_set.update(new_set)
print("after update:", my_set)

# union
union_set = my_set.union(new_set)
print("after union:", union_set)

# difference
diff_set = my_set.difference(new_set)
print("after difference:", diff_set)
# intersection 
intersection_set=my_set.intersection(new_set)
print("after intersection :",intersection_set)
