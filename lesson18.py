#dates
from datetime import date, timedelta, datetime

today = date.today()
print(today)

formatted_date = today.strftime('%a of %d-%m-%Y')
print(formatted_date)

after_forty_days = today + timedelta(days=40) #ctrl + click
print(after_forty_days)

#number of days between two dates
dob= '1990-01-25'

#convert to date object
date_of_birth = datetime.strptime(dob, '%Y-%m-%d')
age = today.year - date_of_birth.year
print('I am', age, 'days old')

age_in_days = datetime.today() - date_of_birth
print(age_in_days.days)