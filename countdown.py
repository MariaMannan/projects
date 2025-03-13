#Project: Countdown timer

#import library of time
import time

#make a function to countdown timer 
def countdown(sec:int):
    while(sec>0):
        #convert input seconds into min and sec
        mins , secs = divmod(sec,60)
        #properly displays timer
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        #creates a delay of 1 sec
        time.sleep(1)
        sec -= 1
    print("Time Over!")

#takes input from user and convert it into int
seconds = int(input("Enter time in seconds: "))
#calls function
countdown(seconds)