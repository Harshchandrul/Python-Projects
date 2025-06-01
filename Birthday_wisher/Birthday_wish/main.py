# ---------------------- Hard Starting Project ---------------------- #
import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. 


# 2. Check if today matches a birthday in the birthdays.csv
# TODO -1  use birthday.csv
birthday_data = pandas.read_csv('birthdays.csv')
birthday_data_dict = birthday_data.to_dict(orient='records')

# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

now = dt.datetime.now()
month = now.month
day = now.day
my_email = "chandruldeveloper@gmail.com"
password = "szae bnce jcdf zxbu"

# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

for person_info in birthday_data_dict:
    if person_info['month'] == month and person_info['day'] == day:
        random_num = random.randint(1, 3)

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"./letter_templates/letter_{random_num}.txt") as letter_file:
            content = letter_file.read().replace('[NAME]', person_info['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(my_email, to_addrs=person_info['email'], msg=f"Subject:Happy Birthday!\n\n{content}")

# HINT: https://www.w3schools.com/python/ref_string_replace.asp
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
