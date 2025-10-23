import random
score=0
attempts=1
while True:
    user_input=input("enter your choice(rock,paper or scissors): ")
    choices=["rock","paper","scissors"]
    computer_choice=random.choice(choices)
    print(f"Computer chose:{computer_choice}")
    if user_input == computer_choice:
        print("Its a tie!")
    elif user_input=="rock":
        if computer_choice=="scissors":
            print("You win!")
            score+=1
    else:
        print("You lost")
    if user_input == "paper":
        if computer_choice == "rock":
            print("You win!")
            score+=1
    else:
        print("you lost")
    if user_input == "scissors":
        if computer_choice=="paper":
            print("You won")
        else:
            print("Invalid input!")
    continue
    play_again=input("Do you want to play again?(y/n):")
    if play_again !='y':
            print(f"your final score is:{score}/{attempts}")
            break
    else:
        attempts+=1
