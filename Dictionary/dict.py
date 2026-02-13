# dictionary uses hashing technique 
# it store data in key value pairs 
# changeble and unordered
# fast access bu using help of keys 

my_dict = {"name":"sunny","age":35,"country":"india"}
print("my dictionary:", my_dict)

# accesing keys
a=my_dict.keys()
print("all keys ",a)

# accesing values
b=my_dict.values()
print("all values:", b)

# updating 
my_dict["name"]="remo"
print(f" after update : {my_dict}")
