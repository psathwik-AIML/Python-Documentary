# comma separated values is know as csv
# it is a file that looks like a json file 
# columns and rows like a table 
# columns are separated by the commas
# before doing csv files we need to import 
import csv
# open a file in write mode 
file=open("file.csv","w",newline="")
#newline remove unnecessary blanks
# create a writer object
write=csv.writer(file)
# now write
write.writerow(["Name","Age","Skills"])
write.writerow(["Remo","22","Python"])
write.writerow(["Doom","22","Python"])
write.writerow(["Anonymous","22","Python"])
file.close()
# reading all mode
file=open("file.csv","r")
read=csv.reader(file)
next(read)
for row in read:
    print(row[0])
# read works like a list of lists 
file.close()
# append mode 
file=open("file.csv","a",newline="")
writer=csv.writer(file)
writer.writerow(["Sunny","21","Java"])
file.close()
