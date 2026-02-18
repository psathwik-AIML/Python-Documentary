import random
choices=["rock","paper","scissors"]
while True: 
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock / paper / scissors ? :").lower()
        
    if(player==computer):
        print(f"player : {player}")
        print(f"computer : {computer}")
        print("Tie..!")
    elif(player=="rock"):
        if(computer=="paper"):
            print(f"player : {player}")
            print(f"computer : {computer}")
            print("You Loose")
        if(computer=="scissors"):
            print(f"player : {player}")
            print(f"computer : {computer}")
            print("You won")
    elif(player=="paper"):
        if(computer=="scissors"):
            print(f"player : {player}")
            print(f"computer : {computer}")
            print("You Loose")
        if(computer=="rock"):
            print(f"player : {player}")
            print(f"computer : {computer}")
            print("You won")
    elif(player=="scissors"):
        if(computer=="rock"):
            print(f"player : {player}")
            print(f"computer : {computer}")
            print("You Loose")
        if(computer=="paper"):
            print(f"player : {player}")
            print(f"computer : {computer}")
            print("You won")
    play_again=input("want to play again : yes/no").lower()
    if(play_again!="yes"):
        break
print("Bye see u agin ")

    