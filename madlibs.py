
#project 1
#Madlibs project

noun : str = input("Enter a noun or subject: ")
verb : str = input("Enter a verb: ")
adjective : str = input("Enter an adjective: ")
place : str = input("Enter any place: ")

madlibs = f"""A {adjective} brown {noun} is {verb} in the {place}.
 He was {verb} happily. Sometimes he thinks himself {adjective} 
 and went to his friend's {place} for a better {verb}."""

print(madlibs)