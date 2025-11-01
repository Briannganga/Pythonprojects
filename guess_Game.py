import random
#ask user to enter their value.
user_input=input("guess a number: ")
#validate user input
if user_input.isdigit():
    user_input=int(user_input)
    if user_input >9:
        print("enter a value from 0 to 9 ")
else:
    print("enter an integer from 0 to 9 ")
#generate random numbers and save to variable r.
r=random.randrange(10)
#make a loop to allow guesses.
guess=1
while  user_input!=r :
    user_input=input("try again: ")
    if user_input.isdigit():
        user_input=int(user_input)
        if user_input >9:
            print("enter a value from 0 to 9 ")
    else:
        print("enter an integer from 0 to 9 ")
    guess+=1
    continue
if user_input==r:
    print("Correct")
    print("you got it in "+str(guess)+" guesses")
