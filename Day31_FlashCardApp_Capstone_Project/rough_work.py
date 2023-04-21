import csv

import pandas as pd
import random

# ---------------------------- READ DATA ------------------------------- #
data = pd.read_csv("../Day31_FlashCardApp_Capstone_Project/flash_card_project/data/french_words.csv")
data_dict = data.to_dict(orient="records")
# print(data_dict[0]["French"])
print(random.choice(data_dict))

# with open("../Day31_FlashCardApp_Capstone_Project/flash_card_project/data/french_words.csv", "r") as file:
#     data = csv.DictReader(file)
#     data_ls_dict = list(data)
#     print(data_ls_dict)

words_to_remove = []

# When correct button is clicked
answers = []


