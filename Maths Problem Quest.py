import random
import time
from colorama import init, Fore, Style 

# Constants
operators = ["+", "-", "*"]
min = 0
max = 0
total = 10
max_wrong_attempts = 5

def get_level():
    while True:
        try:
            level = int(input("Choose Difficulty level (1 for Easy, 2 for Medium, 3 for Hard): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter a valid level (1, 2, or 3).")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")

def generate_problem():
    left = random.randint(min, max)
    right = random.randint(min, max)
    operator = random.choice(operators)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)  # eval evaluates the string as a Python expression
    return expr, answer

def main():
    print(Fore.CYAN + "Welcome to Brainy Math Quest!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Instructions:" + Style.RESET_ALL)
    print("1. Choose a difficulty level.")
    print("2. Solve the given ten math problems.")
    print(f"3. You have a maximum of {max_wrong_attempts} wrong attempts before the quiz ends.\n")

    level = get_level()

    global min, max
    if level == 1:
        print("Difficulty level: Easy\n")
        min = 2
        max = 11
    elif level == 2:
        print("Difficulty level: Medium\n")
        min = 5
        max = 23
    elif level == 3:
        print("Difficulty level: Hard\n")
        min = 10
        max = 40

    wrong = 0
    input("Press Enter to start!")
    print("---------------------")

    start_time = time.time()  # gives us current time

    for i in range(total):
        expr, answer = generate_problem()
        while True:
            guess = input(f"Problem #{i + 1}: {expr} = ")
            if guess == str(answer):
                break
            else:
                wrong += 1
                if wrong >= max_wrong_attempts:
                    print(Fore.RED + f"Quiz Failed! You have given {max_wrong_attempts} wrong answers." + Style.RESET_ALL)
                    return
                else:
                    print(Fore.LIGHTRED_EX + f"Wrong answer! You have {max_wrong_attempts - wrong} attempts left." + Style.RESET_ALL)

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print("---------------------")
    print(Fore.GREEN + f"Nice work! You finished in {total_time} seconds!" + Style.RESET_ALL)
    input("Press Enter to exit...")

if __name__ == "__main__":

    main()
