## Sending Email with Python
import smtplib
import random
import datetime as dt

my_email = "codeemail@gmail.com"
password = "Enter password here"
# Please update email address list of can read from a data file as necessary...
to_emails = ["####@gmail.com", "m#####p@gmail.com", "code_tester@hop.com"]


# grab_random_quote
def grab_random_quote():
    with open("quotes.txt") as quote_data:
        data = quote_data.read().strip().split("\n")
        print(type(data))
        # print(data[0])
        # print(random.choice(data))
        return random.choice(data)


print(grab_random_quote())

# Check day is Friday
now = dt.datetime.now()
wod = now.weekday()
print(type(wod))
if wod == 4:
    print("Today is Friday.")

    quote = grab_random_quote()
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_emails,
                            msg=f"Subject: Python greetings!\n\nQuote of the day:\n\n {quote}.\n\nEnjoy!!!")
