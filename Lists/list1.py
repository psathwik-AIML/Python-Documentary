# list is a collection of data stored in single variable
# list is a ordered and changeble 
list=["code","remo","nut","egg","camera"]
print(f"The List is :{list}")
# methods :

# length of list
print(f"Length of collection: {len(list)}")
# add at end 
list.append("human")
print(f"after append list is :{list}")
# remove at end 
list.pop()
print(f"after pop list is :{list}")
# remove particular element in list 
list.remove("code")
print(f"after remove list is :{list}")
# sorting list 
list.sort()
print(f"after sort list is :{list}")
#clear all 
list.clear()
print(f"after clear list is :{list}")

# looping all 
games=["cricket","volleyball","chess","shuttle"]

for i in games:
    print(i)
