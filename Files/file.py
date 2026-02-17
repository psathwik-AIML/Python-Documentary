import os

path="C:\\Users\\Windows\\SATHWIK\\Documents\\PYTHON\\Python Documentary\\Dictionary"

if(os.path.exists(path)):
    print("path is correct")

if(os.path.isfile(path)):
    print("it is a file")

if(os.path.isdir(path)):
    print("it is a folder")

