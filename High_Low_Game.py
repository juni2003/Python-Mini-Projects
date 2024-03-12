import random  
from colorama import init, Fore , Style
init()  
rand1 = random.randint(0, 10)

print("\n\n>>Let's play high low game\n >>Rules: Numbers are choosen randomly and you have to guess weather next number is higher or lower. Range(0 to 10)")

print(">>Let's start!!!")


score=0

while True:
    while True:
            rand2 = random.randint(0, 10)
            if rand2 != rand1:
                break
    print("Current Number:",rand1,end="")
    print("\t\tYour score:",score,end="")
    Guess = input("\nGuess higher(H) or lower(L) or Quit(Q): ")
    if Guess.upper() == "H" or Guess.upper() == "L":

        if rand2>rand1:
            if Guess.upper()=="H":
                print(Fore.GREEN + Style.BRIGHT +" Correct! Welldone!\n"+ Style.RESET_ALL) 
                                                                    
                score =int(score+10)
                rand1=rand2
            else:
                print("Oops! Better luck next time!")
                print("Game Over! Next number is",rand2)
                print("Final Score :",score)
                quit()
        elif rand2<rand1:
            if Guess.upper()=="L":
                print(Fore.GREEN + Style.BRIGHT +" Correct! Welldone!\n"+ Style.RESET_ALL)
                score =int(score+10)
                rand1=rand2
            else:
                print("Oops! Better luck next time!")
                print("Game Over! Next number is",rand2)
                print("Final Score :",score)
                quit()
        elif Guess.upper()=="Q":
            print("You've quit the game. Final score: "+str(score))
        else:
            print("Oops! Better luck next time!")
            print("Game Over! Next number is",rand2)
            print("Final Score :",score)
            quit()
    else:
        if Guess.upper()=="Q":
            print("You've quit the game. Final score: "+str(score))
            quit()
        else:
            print("Invalid input! Please input H ,L or Q. Exiting...")
            print("Your Final Score :",score)
            quit()
    input("Press Enter to exit...")       #Waits for user input before closing cmd window
        

