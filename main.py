import datetime as dt
import pandas as pd
import random
import smtplib

Email_Id = 'Your MailID'
Password = "Your Password"

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month , today_day)


data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["date"]) : data_row 
                  for (index, data_row) in data.iterrows()
                  }

for i in birthdays_dict:
    if i == today:
        birthday_person = birthdays_dict[today]
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
            content = letter_file.read()
            contents = content.replace("[NAME]" , birthday_person["name"])
    

        with smtplib.SMTP("smtp.gmail.com" , port= 587) as email:
                email.starttls()
                email.login(user= Email_Id , password= Password)
                email.sendmail(from_addr= Email_Id ,
                            to_addrs= birthday_person["email"] , 
                            msg = f"Subject : Happy Birthday \n\n{contents}")
print("EMAIL SENDED")

