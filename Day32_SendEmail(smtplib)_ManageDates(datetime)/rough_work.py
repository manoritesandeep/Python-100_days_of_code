"""
correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"
"""
#
#
# import datetime as dt
# import random
#
# now = dt.datetime.now()
# wod = now.weekday()
# print(type(wod))
# if wod == 4:
#     print("Today is Friday.")
#
#
# # grab_random_quote
# def grab_random_quote():
#     with open("day_motivational_email/quotes.txt") as quote_data:
#         data = quote_data.read().strip().split("\n")
#         print(type(data))
#         # print(data[0])
#         # print(random.choice(data))
#         return random.choice(data)
#
# print(grab_random_quote())

##### Birthday wisher Project #####
#
# import pandas as pd
# import datetime as dt
#
# data = pd.read_csv("../Day32_SendEmail(smtplib)_ManageDates(datetime)/birthday_wisher/birthdays.csv")
# # print(data)
# print(data['name'])
# print(data[data['name'] == "gmail"])
# print(type(data['year']))
# print(data["year"])

# data["year"] = data['year'].astype(int)
# data['year'] = pd.to_numeric(data['year'])
# print(data['year'])
# print(type(data['year']))
# df = data
# df['date'] = pd.to_datetime(dict(year=data.year,
#                                  month=data.month,
#                                  day=data.day))
# print(df.month)
# month = df.month
# day = df.day
# bday_date = (month, day)
# print(f"bday date = {bday_date}, type: {type(bday_date)}")
#
#
#
# today = dt.datetime.now()
# today_date = (today.month, today.day)
# print(f"today_date: {today_date}")

# if bday_date[0][0] == today_date[0]:
#     print(f"Its a birthday!!!")
import random
import re

# random_letter_num = random.randint(1, 3)
# print(random_letter_num)
#
# birthday_name = [name for name in data['name']]
# print(birthday_name)
#
# if today_date in birthday_day:
#     print("Its your birthday!!!")
#     # print(birthday_day.values())
#     # send wishes
#     # wishes()


# check
# is_bday = True
#
# while is_bday:


#
# is_bday = True
# while is_bday:
#     for b_date in birthday_day:
#         if today_date != b_date:
#             is_bday = False
#         else:   # today_date == b_date
#             print("It's a birthday!!!")
#             # print(f"Name: {birthday_day[b_date]['name']}")
#             # print(f"Email: {birthday_day[b_date]['email']}")
#             wishes(name=birthday_day[b_date]['name'].title(),
#                    email_id=birthday_day[b_date]['email'])
#
# for b_date in birthday_day:
#     print(b_date)
#     print(f"Name: {birthday_day[b_date]['name']}")
#     if today_date == b_date:
#         print(b_date)
#         print("It's a birthday!!!")
#         print(f"Name: {birthday_day[b_date]['name']}")
#

# is_bday = True
# while is_bday:
#     for b_date in birthday_day:
#         print(b_date)
#         # print(f"Name: {birthday_day[b_date]['name']}")
#         if today_date == b_date:
#             print("It's a birthday!!!")
#             print(f"Name: {birthday_day[b_date]['name']}")
#             # print(f"Email: {birthday_day[b_date]['email']}")
#             # wishes(name=birthday_day[b_date]['name'].title(),
#             #        email_id=birthday_day[b_date]['email'])
#         else:   # today_date == b_date
#             print("Not a day")
#     else:
#         is_bday= False

# Enter password here















