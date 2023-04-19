import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# ask user input
name = input("Enter your name:").upper()

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(alpha_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.
word_list = [alpha_dict[alphabet] for alphabet in name if alphabet in alpha_dict.keys()]
print(word_list)
