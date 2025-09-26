# python lists used to store more values in a single variable
# indexing starts from 0
fruits=["apple","mango","papaya","banana"]
print("Fruits :",fruits)
# accesing
fruits[1]
# update
fruits[2]="grapes"
print("Updated list: ",fruits)
# adding item to existed list
fruits.append("guava")
# removing from list
fruits.remove("grapes")
# accessing all at once one by one
print("All fruits list: ")
for fruit in fruits:
    print(fruit)
# list length
print(f"Length of list is: {len(fruits)}")
# slicing in a list 
# slicing is taking sub part from list
print("Slice" ,fruits[1:3])
# insert in list
fruits.insert(1, "orange")
print(fruits)
# pop is used for removing last item in list
fruits.pop()
print("pop:",fruits)
nums = [5, 2, 9, 1]
nums.sort()
# [1, 2, 5, 9]
nums.reverse()
# [9, 5, 2, 1]

