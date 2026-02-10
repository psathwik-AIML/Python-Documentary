print("Mini Calculator Program :")
print("...........................")
operator=input("Enter Operator (+,-,*,/)  :")
first=int(input("Enter First  Number :"))
second=int(input("Enter Second Number :"))

if(operator=="+"):
    result=first+second
    print(result)
elif(operator=="-"):
    result=first-second
    print(result)
elif(operator=="*"):
    result=first*second
    print(result)
elif(operator=="/"):
    result=first/second
    print(result)
else:
    print("The operator is mismatch")
