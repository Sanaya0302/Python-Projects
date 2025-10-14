import random
while True:
    user_input=input("Choose rock, paper or scissors: ")
    choise=["rock","paper","scissors"]
    computer_input=random.choice(choise)
    print("you chose",user_input,"the computer chose",computer_input)
    if user_input==computer_input:
        print("It's a tie!")
    elif user_input=="rock":
        if computer_input=="paper":
            print("You lost!")
        else:
            print("You won!")
    elif user_input=="paper":
        if computer_input=="rock":
            print("You won!")
        else:
            print("You lost!")
    elif user_input=="scissors":
        if computer_input=="rock":
            print("You lost!")
        else:
            print("You won!")
    play_again=input("Do you want to play again? y/n: ")
    if play_again !="y":
        break