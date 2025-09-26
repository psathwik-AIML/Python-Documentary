# use ful for random generation 
import random
# random number  in between 1 and 10
print(random.randint(1,10))
# select randomly in list 
colors=['red','blue','green','orange','gold']
print(random.choice(colors))
# before shuffling 
print(colors)
# after shuffling 
random.shuffle(colors)
print(colors)


