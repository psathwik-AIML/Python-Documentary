#  File handling ante:
# Python lo open, write, read, and close cheyatam file ni.
# File ante text document, like .txt or .csv.
# open file in write mode
file=open("file.txt","w")
# write some thing
file.write("Hello sathwik \nToday topic is file handling")
# close file after using
file.close()

# read what u wrote
# open file in read mode 
file=open("file.txt","r")
# read the file 
print(file.read())
file.close
# adding  list to a file 
fruits=["banana","apple","orange","pineapple","water melon"]
file=open("file.txt","w")
# loop through list
for fruit in fruits:
    file.write(fruit+"\n")
file.close()
# read file
print("file data:--------->")
file=open("file.txt","r")
print(file.read())
file.close()
# add with out deleting 
file=open("file.txt","a")
file.write("grapes")
file.close()

# imp:strip() it removes unwanted spaces and \n
# for multiple lines add at once 
# readlines() ante motham data ni oka list lo isthadhi  including \n