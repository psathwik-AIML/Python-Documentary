# real world all data is stored in the format of json only 
import json
data={
    "name":"remo",
    "age":31,
    "fail":False,
    "work":None
}
# normal 
print(data)
real=json.dumps(data)
# json 
print(real)
# write python to json file 
file=open("file.json","w")
json.dump(data,file)
file.close()
# read json file 

file = open("file.json", "r")   
student = json.load(file)         
file.close()                      

print(student)
print(student["name"])            

# modification of json file 
file = open("file.json", "r")
student = json.load(file)
file.close()

student["age"] = 23                          

file = open("file.json", "w")
json.dump(student, file)
file.close()
