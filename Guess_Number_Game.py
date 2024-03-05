import random  

ending_range = input("Enter range for random number from 0 to : ")

if ending_range.isdigit():
    ending_range=int(ending_range)   
    if ending_range<=0:
        print("Invalid input! Please type a number greater than zero next time.")
        quit()
else:
    print("Invalid input! Please type a number next time.")
    quit()

random_number = random.randint(0, ending_range)  

guesses = 5
print("\nLets Play! You have 5 tries.\n")
while True:
    guesses = guesses-1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Invalid inpput! Please type a number next time.")
        continue    
    if user_guess==random_number:
        print("Congratulations! You guessed it right.\nYou Won!!!")
        break
    else:
        print("Wrong guess",end=" ")
        if user_guess>random_number:
            print("Try a Lower number.")
        if user_guess<random_number:
            print("Try a Higher number.")
        print("You have", guesses , "tries left.\n")
        if guesses==0:
            print("You Lose! You didn't guessed the number. Better luck next time.")
            break
        
    
