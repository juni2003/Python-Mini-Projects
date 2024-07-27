import turtle
import time
import random

WIDTH , HEIGHT = 700, 600
COLORS = ["red", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

def get_nbr_of_racers():
    racers = 0
    while True:
        racers =input("Enter the number of races (2-10): ")
        if racers.isdigit():
            racers =int(racers)
        else:
            print("Input must be a number. Try Again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number must be in range 2 to 10. Try Aain!")

def get_nbr_of_players(racers):
    players = 0
    while True:
        players =input(f"Enter the number of players betting (2-{racers}): ")
        if players.isdigit():
            players =int(players)
        else:
            print("Input must be a number. Try Again!")
            continue
        if 2 <= players <= racers:
            return players
        else:
            print("Number must be in range 2 to 10. Try Aain!")

def players_betting(players,colors):
    duplicate_colors = colors[:]
    players_bet = []
    players_name=[]
    names_color = {}  #dictionary of players coresponding to choosen color
    for i in range(players):
        name = input(f"Enter name for Player# {i+1}: ").strip()
        players_name.append(name)
    print("Choose color of Turtle for each player from these :",duplicate_colors)
    for i in range(players):
        while True:
            choice = input(f"{players_name[i]} choose your Turtle's color: ").strip()
            choice = choice.lower()
            if choice  in duplicate_colors:
                names_color[players_name[i]] = choice    #Add the choice of color with player name in dictionary
                duplicate_colors.remove(choice)
                break
            else:
                print("Invalid input input must be from this list :" ,duplicate_colors)
        players_bet.append(choice)
    return players_name, players_bet, names_color
            
            
def race(colors,names_colors):
    turtles = create_turtles(colors ,names_colors)

    while True:
        for racer in turtles:
            distance = random.randrange(5, 20)
            racer.forward(distance)

            x, y = racer.pos()  #get racer position
            if y >= HEIGHT //2 - 10:
                return colors[turtles.index(racer)]  #Get winner color



def create_turtles(colors, names_colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)

    #Drawing Finish Line 
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.setpos(-WIDTH // 2, HEIGHT // 2 - 10)
    finish_line.pendown()
    finish_line.forward(WIDTH)
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.forward(50)
    finish_line.right(90)
    finish_line.forward(10)
    finish_line.write("Finish Line", align="center", font=("Arial", 12, "normal"))

    #Displaying players name below the turtle they bet
    

    for i, color in enumerate(colors):
        for name, chosen_color in names_colors.items():
            if chosen_color == color:
                name_display = turtle.Turtle()
                name_display.hideturtle()
                name_display.penup()
                # Adjust the position slightly below the turtle
                name_display.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 10)
                # Write the name associated with the current color
                name_display.write(name, align="center", font=("Arial", 12, "bold"))

    return turtles

    

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Speedway!")
    screen.bgcolor("ivory")  

def countdown():
    countdown = turtle.Turtle()
    countdown.hideturtle()
    countdown.penup()
    countdown.setpos(0, 0)
    for i in range(3, 0, -1):
        countdown.clear()
        countdown.write(i, align="center", font=("Arial", 48, "normal"))
        time.sleep(1)
    countdown.clear()
    countdown.write("Go!", align="center", font=("Arial", 48, "normal"))
    time.sleep(1)
    countdown.clear()

def main():
    racers = get_nbr_of_racers()
    players = get_nbr_of_players(racers)
    init_turtle()
    
    random.shuffle(COLORS)
    colors = COLORS[:racers]   #choose colors from list upto number of racers
    players_name, players_bet, names_colors = players_betting(players,colors)
    countdown()
    winner = race(colors, names_colors)
    if winner in players_bet:
        index = int(players_bet.index(winner))
        print(f"Player {players_name[index]} bet on {winner} turtle and won the bet")
    else:
        print(f"No player wins the bet as {winner} turtle won the race")

    time.sleep(2)

main()


