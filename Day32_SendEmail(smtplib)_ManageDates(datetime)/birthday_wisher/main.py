##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# Idea: combining GUI Tkinter project with this to add details and save to csv ...
# create app and share

import pandas as pd
import datetime as dt
import random
import smtplib

data = pd.read_csv("birthdays.csv")
# dict = {new_key: new_value for (index, data_row) in data.iterrows()}


def wishes(name: str = None, email_id: str = None):
    with open(f"../birthday_wisher/letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        letter_data = letter.read().replace("[NAME]", name)
        # return letter_data.replace("[NAME]", name)
        # letter_data = letter_data.replace("[NAME]", name)

        my_email = "EMAIL HERE"
        password = "PASSWORD HERE"

        # Send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_id,
                                msg=f"Subject: Happy Birthday!!!\n\n {letter_data}\n\nEnjoy!!!")


# wishes(name="bob")

birthday_day = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
today = dt.datetime.now()
today_date = (today.month, today.day)

for b_date in birthday_day:
    # print(b_date)
    if today_date == b_date:
        print("It's a birthday!!!")
        # print(f"Name: {birthday_day[b_date]['name']}")
        # print(f"Email: {birthday_day[b_date]['email']}")
        wishes(name=birthday_day[b_date]['name'].title(),
               email_id=birthday_day[b_date]['email'])

