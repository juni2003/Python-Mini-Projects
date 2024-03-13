import time

name = input("Enter your name: ")
print("Welcome,",name," Your journey starts now...")
time.sleep(3)
print("You find yourself standing in the middle of a desolate road enveloped by darkness...")
time.sleep(5) 
answer = input("You're faced with two paths ahead.\nWill you venture left or right? (left/right) ").lower()

if answer == "left":
    print("Choosing left, drawn by the distant sound of water, you tread the riverbank. Hours passing...")
    time.sleep(5)
    print("Darkness is griping around you...")
    time.sleep(4)
    answer = input("You must decide whether to walk or swim. (walk/swim): ").lower()
    
    if answer == "walk":
        print("You chose to walk along the riverbank, but hours turned into an eternity, and your water supply depleted...")
        time.sleep(5)  
        print("Exhausted and defeated, you stumble upon a hidden cave entrance...")
        time.sleep(4)  
        print("Curiosity getting the better of you, you enter the cave and encounter two paths diverging into darkness.")
        time.sleep(4)  
        answer = input("Which path will you choose? (narrow/steep) ").lower()

        if answer == "narrow":
            print("You chose the narrow passage, but it quickly narrows down to an impassable crevice...")
            time.sleep(5) 
            print("Trapped and alone, your journey ends here.")
        elif answer == "steep":
            print("Opting for the steep descent, you find yourself tumbling into darkness...")
            time.sleep(5) 
            print("Your fall is relentless, and your journey ends in the depths below.")
        else:
            print("Not a valid option. Game over!")
    elif answer == "swim":
        print("Braving the river's currents, you plunge into the water, each stroke a battle against the relentless flow...")
        time.sleep(5)  
        print("Suddenly, a shadow emerges from the depths, sealing your fate...")
        time.sleep(4)  
        print("You've encountered a river-dwelling predator, and your journey comes to an abrupt end.")
    else:
        print("Not a valid option. Game over!")

elif answer == "right":

    print("You turn right and spot a faint glow emanating from the corner...")
    time.sleep(4) 
    print("As you approach, a shimmering portal comes into view...")
    time.sleep(4) 
    answer = input("Do you dare to leap into the unknown, or will you retreat and seek another path? (jump in/back) ").lower()
    
    if answer == "jump in":
        print("With resolve, you leap into the swirling vortex, and suddenly, the landscape shifts around you...")
        time.sleep(4) 
        print("You find yourself surrounded by towering mountains and swirling dust...")
        time.sleep(4) 
        answer = input("Will you explore or attempt to return through the portal? (explore/go back) ").lower()
        
        if answer == "explore":
            print("As you venture into the desolate landscape, an ominous voice echoes through the terrain... ")
            time.sleep(4) 
            answer = input("Do you choose to hide or flee? (hide/flee) ").lower()
            
            if answer == "hide":
                print("You attempt to conceal yourself, but your efforts are futile against the prehistoric predator that discovers your presence...")
                time.sleep(5) 
                print("In the jaws of the dinosaur, your journey comes to a tragic end.")
            elif answer == "flee":
                print("You run with all your might, but the thunderous footsteps behind you only grow louder...")
                time.sleep(5) 
                print("In the end, the relentless pursuit of the dinosaur proves insurmountable. Your journey meets a swift and untimely demise.")
            else:
                print("Not a valid option. Game over!")
                
        elif answer == "go back":
            print("You attempt to return through the portal, but its shimmering surface remains impassable...")
            time.sleep(5)
            print("Trapped in a loop of time, your existence fades into oblivion. Game over!")
        else:
            print("Not a valid option. Game over!")

    elif answer == "back":
        print("You decide to retreat from the portal and return to the main road. Along the way, you encounter a weary traveler seeking assistance...")
        time.sleep(5)
        answer = input("Will you offer your help or continue on your journey? (help/keep moving) ").lower()
        
        if answer == "help":
            print("Your act of kindness proves rewarding as the traveler provides you with a means of transportation... ")
            time.sleep(5)
            print("Safely reaching your destination, you emerge victorious.")
        elif answer == "keep moving":
            print("You choose to press onward, but fate has other plans...")
            time.sleep(5)
            print(" As you journey forward, you encounter a perilous obstacle, sealing your fate. Your journey ends here.")
        else:
            print("Not a valid option. Game over!")
            
    else:
        print("Not a valid option. Game over!")

else:
    print("Not a valid option. Game over!")
input("Press Enter to exit...")
