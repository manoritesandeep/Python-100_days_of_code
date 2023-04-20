from tkinter import *


def convert():
    print("converting test")
    distance_km = int(c_input.get()) * 1.609
    text_result2.config(text=f"{distance_km}")
    # return distance_km


# Window
window = Tk()
window.title("Miles to Km converter")
window.minsize(width=300, height=200)


# Label
my_label = Label(text="This app converts Mile to Km")
my_label.grid(column=0, row=0)

# Entry
c_input = Entry(width=10)
c_input.get()
c_input.grid(column=1, row=2)

# Text
text_miles = Label(text="Miles")
text_miles.grid(column=2, row=2)

# Text 2
text_result1 = Label(text="is equal to")
text_result1.grid(column=0, row=3)

# Text result return
text_result2 = Label(text="0")
text_result2.grid(column=1, row=3)

# Text KM
text_kms = Label(text="Km")
text_kms.grid(column=2, row=3)

# Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=5)



window.mainloop()
