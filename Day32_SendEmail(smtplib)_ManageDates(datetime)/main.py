# """
# correct smtp address for your email provider:
#
# Gmail: smtp.gmail.com
#
# Hotmail: smtp.live.com
#
# Outlook: outlook.office365.com
#
# Yahoo: smtp.mail.yahoo.com
#
# If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"
# """

# import smtplib
#
# my_email = "code@gmail.com"
# password = "Enter password here"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="code_tester@yahoo.com",
#                         msg="Subject:Hello\n\nHappy Birthday!!! Have fun!!!")
#
#


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(type(year))
print(f"Month: {month}, Year:{year}, day of week(starts: 0 - Monday):{day_of_week}")
print(now)
print(type(now))

# Custom datetime objects
date_of_birth = dt.datetime(year=1992, month=6, day=15, hour=9)
print(date_of_birth)

