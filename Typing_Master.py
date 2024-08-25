#Remember to create text file with name Rand_text and place it in correct directory
import curses
from curses import wrapper #used to initialize the module and run commands
import time
import random
import winsound  #Library for sound


def play_sound(correct=True):
    if correct:
        winsound.Beep(1000, 50)  # High beep for correct
    else:
        winsound.Beep(500, 50)   # Low beep for incorrect


def start_screen(stdscr):
    
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Initializing color 

    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Speed Test! Let's see your typing skills...")
    instructions = ( 
        "Instructions:\n"
        "- Type the text as accurately and quickly as possible.\n"
        "- Your WPM (Words Per Minute), Accuracy and a Timer will be displayed during the test.\n"
        "- Press 'Esc' at any time to exit the test.\n"
        "- DO NOT minimize or maximize the screen, or the test will restart.\n"
    )
    stdscr.addstr(2, 0, instructions, curses.color_pair(3))  #Here 1 is for row and 0 for coloumn
    stdscr.addstr("Press any key to begin...")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    last_line = len(target.splitlines())

    correct_chars = sum(1 for i, char in enumerate(current) if i < len(target) and char == target[i])

    accuracy = (correct_chars / max(len(current), 1)) * 100  # Calculate accuracy percentage
    stdscr.addstr(last_line + 1, 0, f"WPM : {wpm}  Accuracy: {accuracy:.2f}%")    #ensures WPM and accuracy always placed below last line


    for i, char in enumerate(current): #enumerate func gives index and value respectedly
        
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)


        screen_height, _ = stdscr.getmaxyx()
        row = i // curses.COLS
        col = i % curses.COLS
        if row < screen_height:
            stdscr.addstr(row, col, char, color)


def load_text(): #Remember to create file with name Rand_text.txt
    with open("Tying_Master.txt", "r") as file:
        lines = file.readlines()    #Creates a list of all the lines in the files
        return random.choice(lines).strip()     #.Strip() func removes the end /n which is present at the end of each line


def typing_test(stdscr):
    while True:
        for i in range(3, 0, -1):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Get ready! Starting in {i}...")
            stdscr.refresh()
            time.sleep(1)

        target_text = load_text()
        current_text = []
        wpm = 0
        start_time = time.time()
        stdscr.nodelay(True)

        last_screen_size = stdscr.getmaxyx()  # Store the initial screen size to handle minimize and maximize   
        test_running = True  # Flag to control the test loop
 

        while test_running:
            time_elapsed = max(time.time() - start_time, 1)
            wpm = round( (len(current_text) / (time_elapsed / 60))  / 5 )
            if stdscr.getmaxyx() != last_screen_size:
             break             # If screen is resized, break and restart the test again
               
            stdscr.clear()

            # Format for timer is MM:SS
            minutes = int(time_elapsed) // 60
            seconds = int(time_elapsed) % 60
            formatted_time = f"{minutes:02}:{seconds:02}"
            stdscr.addstr(2, 30, f"Timer: {formatted_time} Sec")
            stdscr.move(0, 0)  #sets cursor back after setting timer

            display_text(stdscr, target_text, current_text, wpm)
            stdscr.refresh()

            if "".join(current_text) == target_text:  #join converts list to string joining them with "" the character inside quotations
                stdscr.nodelay(False)
                break  #exits from function if completed the text
            
            try:
                key = stdscr.getkey()    #This line causing delay waiting for user to enter key and then continue
            except:
                continue   #Brings back to While loop (While True)

            if len(key) == 1 and ord(key) == 27:   #ASCII Code for Esc key So pressing Ecs key exit
                test_running = False
                break
            if key in ("KEY_BACKSPACE", "\b", "\x7f"):
                if len(current_text) > 0:    #If key is BACKSPACE and length is > 0 then delete last character
                    current_text.pop()
            elif len(current_text) < len(target_text):
                current_text.append(key)      #Handle other keys normaly enless it is smaller then target text
                
                # Play sound only when a key is pressed and compared
                correct = key == target_text[len(current_text) - 1]
                play_sound(correct)

        if not test_running:  # If the flag is set to False, break the outer loop
            break
        display_end_message(stdscr, target_text, time_elapsed, wpm)

def display_end_message(stdscr, target_text, time_elapsed, wpm):
    stdscr.clear()
    correct_words = len(target_text.split())  # Calculate number of words
    stdscr.addstr(0, 0, f"Test completed!")
    stdscr.addstr(1, 0, f"You typed {correct_words} words correctly in {int(time_elapsed)} seconds.")
    stdscr.addstr(2, 0, f"Speed: {wpm} WPM")
    stdscr.addstr(4, 0, "Press any key to start a new test or Esc to exit.")
    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        if ord(key) == 27:  # ASCII code for Esc key to exit
            return  # Exit the function and program
        else:
            break  # Exit the loop and restart the typing test
        
        
                

def main(stdscr):   #stdscr is standaed screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK ) #here 1 represents the colors
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    
    start_screen(stdscr) 
    while True:
        typing_test(stdscr)

        stdscr.addstr(2, 0, "Test is completed! Press any key to start again and Esc to exit.")
        key = stdscr.getkey()
        if ord(key) == 27:
            break
    curses.endwin()  # Clean up and return to normal terminal mode
    input("Press Enter to exit...")
wrapper(main)
    