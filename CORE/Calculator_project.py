# calculator code 
# Taking first number from user
first=int(input("Enter first number: "))
#  Taking second number from user
second=int(input("Enter second number: "))
# code for selecting operator
operator=input("Enter operator (+,-,*,/): ")
# addition function
def add(a,b):
    return a+b
# subtraction function
def sub(a,b):
    return a-b
# multiplication function
def mul(a,b):
    return a*b
# division function
def div(a,b):
    return a/b
# store result in a variable
result=0
# logic of code 
if operator=="+":
    result=add(first,second)
elif operator=="-":
    result=sub(first,second)
elif operator=="*":
    result=mul(first,second)
elif operator=="/":
    if(second!=0):
        result=div(first,second)
    else:
        print("can not divide by zero")
else:
    print("choose the correct operator")

print(f"Result is: {result}")