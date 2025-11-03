import random                                                                            comp_score=0
user_score=0
guess=["rock","paper","scissor"]

while True:
        #convert value entered to string and lower case
        user_pick=input("select rock|paper|scissor or q to quit:").lower()

        if user_pick  in guess:
                print("you pick: "+user_pick)
        elif user_pick=="q":
                print("goodbye")
                if comp_score>user_score:
                        print("computer won with "+str(comp_score)+"points")
                else:
                        user_score>comp_score
                        print("you won with "+str(user_score)+"points")
                quit()
        else:
                print("pick the given options!")
                continue
        comp_guess=random.randint(0,2)
        comp_pick=guess[comp_guess]
        print("computer picks: "+comp_pick)
        if user_pick=="rock" and comp_pick=="scissors":
                print("you win")
                user_score+=1
        elif user_pick=="paper" and comp_pick=="rock":
                print("you win")
                user_score+=1
        elif user_pick=="scissor" and comp_pick=="paper":
                print("you win")
                user_score+=1
        elif user_pick==comp_pick:
                print("thats a draw")

        else:
                print("computer wins")
                comp_score+=1
        continue
