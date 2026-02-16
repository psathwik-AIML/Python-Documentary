# exceptional handling 
# events occured during program execution that interupts flow 
try:
    x=int(input("Enter number 1: "))
    y=int(input("Enter number 2: "))
    res=x/y
except Exception as e:
    print("error is :",e)
else:
    print("result is :",res)
finally:
    print("code execution completed")