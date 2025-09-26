# Topic is Nested if else 
country=input("Enter u r country: ")
if country=="india":
    age=int(input("Enter u r age: "))
    if age>=18:
        print("You are Eligible to vote in india")
    else:
        print("You age is low")
else:
    print("You are not allowed to vote")