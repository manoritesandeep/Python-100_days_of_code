from tkinter import *
from tkinter import messagebox
import random
# pip install pyperclip # copy text to clipboard
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in  range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure all fields are completed!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f" These are the details you entered: \nWebsite:{website}"
                                                              f" \nEmail:{email} "
                                                              f"\nPassword:{password} \nDo they look okay?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website},{email},{password}\n")
                # Clear fields once data is added
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Wind
window = Tk()
window.title("Password Manager and Generator")
# window.minsize(width=1000, height=750)
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# Email/Username Label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
# Website Entry
website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
# Email/Username Entry
email_username_entry = Entry(width=55)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "default_email@gmail.com")
# Password Entry
password_entry = Entry(width=37)
password_entry.grid(column=1, row=3)

# Buttons
# Generate Password Button
generate_pwd_button = Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(column=2, row=3)
# Add button
add_button = Button(text="Add", width=47, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
