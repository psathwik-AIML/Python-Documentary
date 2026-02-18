# quiz game 

# all functions 

# create a new quiz 
def new_quiz():
    guesses=[]
    correct_guess=0
    question_num=1
    
    for key in questions:
        print("...............................")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter A / B / C / D :").upper()
        guesses.append(guess)
        correct_guess+=check_answer(questions.get(key),guess)
        question_num+=1
    display_score(correct_guess,guesses)
    
# checks solutions  
def check_answer(answer,guess):
    if(answer==guess):
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
#  display score
def display_score(correct,guesses):
    score=(correct/len(guesses)*100)
    print(f"Your Score is : {str(score)} %")
# play again
def play_again():
    chance=input("ARE YOU WANT TO PLAY AGAIN ? (Y?N)")
    chance=chance.upper()
    if(chance=="Y"):
        return True
    else:
        return False

questions={
    "who is prime minister of india ?":"C",
    "who invented bulb  ?":"B",
    "which is largerst second populated country  ?":"A",
    "how many minutes does a 1 hour had ?":"D"
}

options=[
    ["A.putin","B.kim","C.modi","D.obama"],
    ["A.einstein","B.thomas","C.robert","D.donglee"],
    ["A.china","B.russia","C.india","D.france"],
    ["A.10","B.100","C.45","D.60"]
    ]

new_quiz()

while play_again():
    new_quiz()
print("Bye ......")