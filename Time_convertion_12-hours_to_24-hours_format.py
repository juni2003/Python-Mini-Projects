
def timeConversion(s):
    
    if s[-2:].upper()=="AM":
        temp = s[:2]
        if temp=="12":
            s ="00" +s[2:]
        returntime = s[:-2]
    if s[-2:].upper()=="PM":
        temp =s[:2]
        if temp=="12":
            returntime = s[:-2]
        else:
            num = int(temp)
            if num<12:
                num = num +12
                s = str(num) + s[2:]
                returntime = s[:-2]
    return returntime
        
            
        
        
if __name__ == '__main__':
    print("\nNote: Please enter time in HH:MM:SS AM/PM format.")
    s = input("Enter Time in 12 Hours format: ")
    while not ((s[-2:] == "AM" or s[-2:] == "PM") and 0 <= int(s[:2]) <= 12):
        s=input("Invalid Input\nEnter Time in 12 Hours format again:  ")
    result = timeConversion(s)
    print("Time in 24 Hours format is: " ,result)

