#Project: rock paper scissor game
import random

#taking input from user
user = input("Enter your choice: \n use(r for rock, s for scissor and p for paper): ")
#allowing computer to choose a random value from given choices
computer = random.choice(["r","p","s"])

#Displaying both choices
print(f"user= {user.lower()}")
print(f"computer= {computer}")

#RULE:  r>s , s>p , p>r
if(user.lower()== computer):
    print("It's a tie. :/")

elif(user.lower()=='r' and computer=="s") or (user.lower()=='s' and computer=="p") or (user.lower()=='p' and computer=="r"):
    print("You Won! :)")

else:
    print("You lost! :(")