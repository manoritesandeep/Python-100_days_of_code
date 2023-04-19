import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
# print(df)

# ask user input
name = input("Enter your name:").upper()
# print(f"You entered {name} as the input.")

# 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

# for index, row in df.iterrows():
#     print(row.letter)
#     print(row.code)

alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(alpha_dict)
# print(alpha_dict["D"])
# print(alpha_dict.keys())
# print(alpha_dict.values())


# 2. Create a list of the phonetic code words from a word that the user inputs.
# name = "thomas"
# list_of_words = []
# for alphabet in name.upper():
#     # print(alphabet)
#     if alphabet in alpha_dict.keys():
#         # print(alpha_dict[alphabet])
#         list_of_words.append(alpha_dict[alphabet])
# print(list_of_words)

word_list = [alpha_dict[alphabet] for alphabet in name if alphabet in alpha_dict.keys()]
print(word_list)













