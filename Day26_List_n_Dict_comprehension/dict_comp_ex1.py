"""
use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence
and calculates the number of letters in each word.
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

d = sentence.split()
# print(d)
len_d = [len(l) for l in d]
# print(len_d)

result = {word: len(word) for word in sentence.split()}
print(type(result))
print(result)
# result = {new_key: new_value for (key, value) in dict.items()}

# print(result)
