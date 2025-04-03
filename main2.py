##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import pandas as pd
import random
import smtplib,ssl
right_now=dt.datetime.now()
curr_month=right_now.month
curr_day=right_now.day

df=pd.read_csv("./birthdays.csv")
birth_month=df["month"][0]
birth_day=df["day"][0]

# print(df)
# print(curr_day)
# print(birth_day)
if curr_day==birth_day and curr_month==birth_month:
    # print("hello")
    rand_num=random.randint(1,3)
    with open(file=f"./letter_templates/letter_{rand_num}.txt") as file:
        letter=file.readlines()
        replace=letter[0].replace("[NAME]","Alex")
        letter[0]=replace
        #print(letter[0])
        print(letter)
port=465
PASSWORD="YOUR APP PASSWORD"
MY_MAIL="YOUR EMAIL"

TO_MAIL="TO ADDRESS"
context=ssl.create_default_context()
SMTP_SERVER="smtp.gmail.com"#can change according to senders mail application
#e.g. "smtp.live.com"
with smtplib.SMTP_SSL(host=SMTP_SERVER,port=port,context=context) as connection:
    connection.login(user=MY_MAIL,password=PASSWORD)
    connection.sendmail(from_addr=MY_MAIL,
                        to_addrs=TO_MAIL,
                        msg=f"SUBJECT:Happy Birthday\n\n{letter}")





