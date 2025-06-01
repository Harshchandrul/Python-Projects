# ------------------------ BIRTHDAY WISHER PROJECT ------------------------ #
import random
import smtplib
import datetime as dt

# yandex mail server = smtp.yandex.ru
my_email = "chandruldeveloper@gmail.com"
password = "szae bnce jcdf zxbu"


def send_mail():

    # reading data from quotes.txt
    with open('quotes.txt') as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes).strip()

    # This starts connection with server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # This secures the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="HarshChandrul@yandex.com",
                            msg=f"Subject:Motivation!\n\n{random_quote}"
                            )


# Understanding Datetime module
now = dt.datetime.now()
day_of_week = now.weekday()  # 0 means monday & 1 mean tuesday
if day_of_week == 2:
    send_mail()

# year = now.year
# day = now.day
# month = now.month
# To create new custom datetime object
# date_of_birth = dt.datetime(2007, 3, 1, 4)
# print(date_of_birth)
