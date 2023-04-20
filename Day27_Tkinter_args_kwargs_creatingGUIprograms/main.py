from tkinter import *


def button_click():
    print("I got called")
    new_text = c_input.get()
    # demo_label.config(text="Button clicked")
    demo_label.config(text=new_text)


# Create new GUI window
window = Tk()
window.title("First GUI program")
window.minsize(width=700, height=500)
# adding padding
window.config(padx=25, pady=25)

# Label
demo_label = Label(text="This is demo label", font=("Arial", 24, "bold"))
# demo_label.pack()
# demo_label.place(x=100, y=150)
demo_label.grid(column=0, row=0)
demo_label.config(pady=50, padx=50)

# https://docs.python.org/3/library/tkinter.html#the-packer

# Button
button = Button(text="Click Here", command=button_click)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = Button(text="This is button 2")
new_button.grid(column=2, row=0)

# Entry
c_input = Entry(width=15)
c_input.get()
# c_input.pack()
c_input.grid(column=4, row=2)

# Keep window open
window.mainloop()
