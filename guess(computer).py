#Project: Guess Number(computer)

#importing a library to generate a random number
import random

def guess_number(x : int):
    """This function will generate a random number and will guess users secret number.
    secret number is known to user only.
    user will provide feedback to computer on guessing number"""
#setting range for computer to guess number
    low : int = 1
    high : int = x
    feedback : str = " "

    #loop will run until computer guesses the number correctly.
    while(feedback != "c"):
        #generates random number between range
        guess_number = random.randint(low,high)
        print(f"Is your number is {guess_number}? ")
        #ASKING USER to provide feedback
        feedback = input(f"Please enter your feedback. Press (H) for high, (L) for low and (C) for correct: ").lower()
        #if feedback is high, change range of guessing number to guess it easily
        if(feedback == "h"):
            high = guess_number - 1
        
        #if feedback is low, change range of guessing number to guess it easily
        elif(feedback == "l"):
            low = guess_number + 1
            
    print(f"Yay! Computer has guessed the number {guess_number} correctly.")

#calling this function with a max range of number as input
guess_number(30)