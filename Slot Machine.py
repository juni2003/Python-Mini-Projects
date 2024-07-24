import random
import time

#Global Constants
MAX_LINES = 3
MAX_BET = 300
MIN_BET = 1

ROWS = 3
COLS = 3 

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8 
}

symbol_value = {    #Shows how valueable a symbol is 
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2 
}



def check_winnings(coloumns , lines, bet, values):
    winnings = 0
    winning_lines = []
    #if line = 1 its top line . if line = 2 its top and second line. 
    for line in range(lines):                 #looping through every row
        symbol = coloumns[0][line]            #symbol at first coloumn of current row
        for coloumn in coloumns:               #loop through every coloumn and check that symbol
           symbol_to_check = coloumn[line]    #symbol to check  =  coloumnn at the current row
           if symbol != symbol_to_check:      #if not same then break
               break
        else:  #corresponds to for statement
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings , winning_lines

def get_slot_machine_spin(rows , cols , symbols):
    all_symbols = []   
    for symbol, count in symbols.items():   #items function gives keys and values from dictonary
        all_symbols.extend([symbol] * count)         #count has value of each key like for "A" * 2 it extend "A","A"
        #append function single element to the list and extend adds each element to list

    columns = []    
    for _ in range(cols):                    
        column = random.sample(all_symbols, rows)        #for each coloumn sample() chooses each element randomly rows times like coloumn = ["A" , "B" , "B"]
        columns.append(column)                            #sample function ensures that it doesnt select same value

    return columns

def slot_machine_output(coloumns):
    #We got coloumns list we need to flip it to convert into row
    #Same as we take tranpose of a matrix changing coloumns in rows and viceversa.
    print("Slot Machine is spining...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    for row in range(len(coloumns[0])): #coloumns must be greater then 0
        for i, coloumn in enumerate(coloumns):
            if i != len(coloumns) - 1:
                print(coloumn[row] , end= " | ")
            else:
                print(coloumn[row] , end ="\n")
                time.sleep(1.5)


def deposit():    #to get users input
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("Amount Deposited successfully")
                break
            else:
                print("Amount must be greater then 0.")
        else:
            print("Invalid Input! Input must be a positive number.")        
    
    return amount

def get_nbr_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines < 4:
                break
            else:
                print(f"Lines must be greater then 0 and less then {MAX_LINES} in order to play")
        else:
            print("Invalid Input! Please enter a number.")        
    
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Invalid Input! Please enter a number.")        
    
    return bet


def spin(balance):
    lines = get_nbr_of_lines()
    attempts = 0
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You have insufficient balace to bet that amount.\nYour current balace is: {balance} ")
            attempts += 1
            if attempts >= 3:            #if 3 or more attempts option for more deposit
                more_deposit = input("Would you like to deposit more money (y/n) :")
                if more_deposit.lower() == "y":
                    balance += deposit()
                    print(f"Your New balace is: ${balance}")
                    attempts = 0
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    slot_machine_output(slots)
    winnings , winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)  
    #This is splat or unpack operator it will pass every line from winning_lines list to print function
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        answer = answer.strip()
        if answer.lower() == "q":
            break
        
        balance += spin(balance)
    
    print(f"You left with ${balance}")
    input("Press enter to exit...")


main()
