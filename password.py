#project: Password Generator

#importing random library to generate passwords
import random

print("Welcome to password generator")

#Storing all characters that can be used in password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.';!#$@%^&*0123456789"

#Asking user about number of passwords he want to create
numbers = int(input("Enter how many passwords you want to generate: "))

#asking user about length of password
length = int(input("Please enter length of passwords: "))
print("Here are your passwords:\n ")

#using for loop and random library to generate passwords
for password in range(numbers):
    passwords = ""
    for i in range(length):
        passwords += random.choice(characters)
    print(passwords)