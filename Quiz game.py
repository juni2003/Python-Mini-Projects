print("\n\nWelcome to this quiz\nSubject: Computer Science")

playing = input("Do you want to start?(yes/no) ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score =0
print("Note: Remember always check the spellings before pressing enter\nGood Luck \n")

answer = input("1.What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("2.What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("3.What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("4.What does HDD stands for? ")
if answer.lower() == "hard disk drive":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("5.What does LCD stands for? ")
if answer.lower() == "liquid crystal display":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("6.What does OS stands for? ")
if answer.lower() == "operating system":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("7.What does LAN stands for? ")
if answer.lower() == "local area network":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("8.What does AMP stands for? ")
if answer.lower() == "application porfolio management":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("9.What does API stands for? ")
if answer.lower() == "application programming interface":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
answer = input("10.What does AES stands for? ")
if answer.lower() == "advanced encryption standard":
    print("Correct!")
    score+=1
else:
    print("Incorrect! :(")
print("Quiz Completed!")
if score>8:
    print("Wow! You got "+ str(score)+" questions correct. Great job!")
if score>5 and score<8:
    print("Nice! You got "+ str(score)+" questions correct. Keep it up!")
if score<5:
    print("You got only "+ str(score)+" questions correct. Better luck next time. Try Again!")

