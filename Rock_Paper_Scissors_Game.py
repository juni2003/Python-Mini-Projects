import random
from colorama import init, Fore , Style

init()

user_wins=0
computer_win=0

options = ["rock","paper","paper"]

score_limit=input("Enter score limit: ")
score_limit=int(score_limit)
while True:
    if computer_win >= score_limit or user_wins >= score_limit:
        break
    
    print("\nYour Score:",user_wins,"\t\tComputer Score:",computer_win)
    user_input=input("Enter your choice (rock/paper/scissors) or type 'Q' to quit:").lower()

    if user_input =="q":
        print("You've quit the game.")
        break

    if user_input not in ["rock", "paper","scissors"]:
        print("Invalid Input! ")
        continue     #back to top of loop

    random_number=random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("The computer choose", computer_pick + ".")

    if user_input =="rock"and computer_pick =="scissors":
        print(Fore.GREEN + "You Won!" + Style.RESET_ALL)  # Print "You Won!" in green color
        user_wins += 1
        continue
    elif user_input=="paper" and computer_pick=="rock":
        print(Fore.GREEN + "You Won!" + Style.RESET_ALL)
        user_wins += 1
        continue
    elif user_input =="scissors" and computer_pick=="paper":
        print(Fore.GREEN + "You Won!" + Style.RESET_ALL)
        user_wins += 1
        continue
    elif user_input==computer_pick:
        print("Draw!")
        continue
    else:
        print(Fore.RED + "You Lost!" + Style.RESET_ALL)
        computer_win += 1
    
print("You won",user_wins,"times.")
print("The computer won",computer_win, "times.")
print("Goodbye!")

input("Press Enter to exit...") #Waits for user input befoe closing cmd window
