import random  
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
                print("\033[1mCorrect!\033[0m Welldone!\n") #\033[1m is the ANSI escape code for starting bold text.
                                                                    #033[0m is the ANSI escape code for resetting text formatting to default.
                score =int(score+10)
                rand1=rand2
            else:
                print("Oops! Better luck next time!")
                print("Game Over! Next number is",rand2)
                print("Final Score :",score)
                quit()
        elif rand2<rand1:
            if Guess.upper()=="L":
                print("#\033[1m Correct!\033[0m Welldone!\n")
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
       
        

