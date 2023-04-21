import csv
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_card = {}
data_dict = {}
print(type(data_dict))

from tkinter import *
import pandas as pd

# ---------------------------- READ DATA ------------------------------- #
# data = pd.read_csv("data/french_words.csv")
# raw_file_path = "data/french_words.csv"

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    canvas.after_cancel(flip_timer)
    # print(data_dict[0]["French"])
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(background_image, image=front_img)
    flip_timer = window.after(3000, flip_card)


# ---------------------------- FLIP CARD --------------------------- #

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(background_image, image=back_img)


# ---------------------------- KNOWN WORDS --------------------------- #

def is_known():
    data_dict.remove(current_card)
    print(len(data_dict))
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Window
window = Tk()
window.title("Flashy")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Flash card canvas
"""
Hint: (super) To change the canvas image, you'll need a reference to the image, 
like what we have with the text created in the canvas. 
Then you can set the image attribute using itemconfig().
PhotoImage objects should not be created inside a function. Otherwise, it will not work.
"""
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")  # French
back_img = PhotoImage(file="images/card_back.png")  # English
background_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
# canvas.create_image(400,263, image=back_img)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
# Correct Button
right_img = PhotoImage(file="images/right.png")
correct_button = Button(image=right_img,
                        highlightthickness=0,
                        command=is_known)
correct_button.grid(row=1, column=1)
# Wrong Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img,
                      highlightthickness=0,
                      command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
