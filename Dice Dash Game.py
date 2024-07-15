import random
from colorama import init, Fore, Style

init()  # Initialize Colorama for colors

def roll():
    min = 1
    max = 6
    return random.randint(min, max)

# Game name and rules to guide user
print(Fore.CYAN + "Welcome to Dice Dash!" + Style.RESET_ALL)
print(Fore.YELLOW + "Game Rules:" + Style.RESET_ALL)
print("1. Each player takes turns to roll a dice.")
print("2. Rolling a 1 resets your score for that turn.")
print("3. Rolling a 6 adds 10 points to your score and turn ends.")
print("4. The first player to reach or exceed 50 points wins!")
print("5. All players get one final turn after a player reaches 50 points.")
print("6. In case of a tie, the game ends in a draw.")
print()

player_names = []
max_score = 50

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2 - 4")
    else:
        print("Invalid Input. Try Again.")

player_scores = [0 for _ in range(players)]  # List comprehension adds all players' scores in list

for i in range(players):
    name = input(f"Enter name for Player #{i + 1}: ")
    player_names.append(name)

final_round = False

while True:
    for player_id in range(players):
        print("\n", player_names[player_id] + "'s turn has just started! \n")
        print(player_names[player_id] + "'s Score:", player_scores[player_id], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll dice (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print(Fore.RED + "Dice rolled a 1! Resetting your score for this turn" + Style.RESET_ALL)
                current_score = 0
                break
            if value == 6:
                print(Fore.GREEN + "Wow! You rolled a 6! Adding 10 points and turn ends" + Style.RESET_ALL)
                current_score += 10
                break
            else:
                current_score += value
                print("You rolled a:", value)
            print("Your score is:", current_score)

        player_scores[player_id] += current_score
        print("Your total score is:", player_scores[player_id])

        if player_scores[player_id] >= max_score and not final_round:
            final_round = True

    if final_round:
        break


max_score = max(player_scores)
winners = [player_names[i] for i, score in enumerate(player_scores) if score >= max_score]

if len(winners) > 1:
    print(Fore.BLUE + "\nIt's a tie between: " + ", ".join(winners) + " with a score of: " + str(max_score) + Style.RESET_ALL)
else:
    print(Fore.GREEN + "\n", winners[0], "wins with a score of:", max_score, Style.RESET_ALL)

input("Press Enter to exit...")
