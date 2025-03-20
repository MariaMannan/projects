#Project: Guess Number(user)

#importing a library to generate a random number
import random

def guess_number(x : int):
    """This function will generate a random number and will keep it secret.
    it will ask user to guess it within range. and will provide feedback"""

    #generates random number between range
    random_number = random.randint(1,x)
    guess : int = 0

    #loop will run until user guesses the number correctly.
    while(guess != random_number):
        #ASKING USER to guess the number
        guess = int(input(f"Please enter a number between 1 and {x}: "))
        if(guess < random_number):
            #Providing feedback to user for help in guessing
            print(f"Sorry! Your guess is Wrong. {guess} is too low.")
        elif(guess > random_number):
            print(f"Sorry!Your guess is Wrong. {guess} is too high.")
    print(f"Congratulations! You have guess the number {random_number} right.")

#calling this function with a max range of number as input
guess_number(20)