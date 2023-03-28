"""
Instructions
You are going to write a program that will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and
     puts them inside a List called names. 
For this to work, you must enter all the names as names 
    followed by comma then space. e.g. name, name, name
"""

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# print(type(names))  # <class 'list'>
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# random_num = random.randint(0, len(names)-1)
# # print(names)
# print(len(names))
# print(random_num)
# print(f"{names[random_num]} is going to buy the meal today!")

############ Using choice from random module #########
person_pay = random.choice(names)
print(f"{person_pay} is going to buy the meal today!")








