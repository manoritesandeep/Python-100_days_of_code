import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
# print(data.columns)

# Fur Color and Count
# colors = list(data['Primary Fur Color'].dropna().unique())
# print(type(colors))
# print(data[colors].value_counts())
# print(data[data[colors]].value_counts())
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
