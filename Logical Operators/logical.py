# and 
is_raining=bool(input("Enter weather condition :"))

have_friend=bool(input("Does u r friend is there to play :"))

if(is_raining==False and have_friend==True):
    print("You can play")
elif(is_raining==True or have_friend==True):
    print("Not allowed")

