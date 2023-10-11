import random

def Replay():
    Try_again = int(input("""Do You want to play again?:  
    
1. Yes
2. No
    """)) 

    if Try_again == 1:
        game_play()

    else: 
        print("Thank for playing")

        

def game_play():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = input("Enter your choice::  ")

    print("User choice: ", user_choice)
    print("Computer choice: ", computer_choice)


    if user_choice == computer_choice:
        print("Tie")
        Replay()
        

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win")
        Replay()

       
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win")
        Replay()

       
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win")
        Replay()


    else:
        print(f"Computer wins! Computer's choice is {computer_choice}")
        Replay()


game_play()