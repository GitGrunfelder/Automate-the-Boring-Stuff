'''Uses Regex to find dates, and uses some logic to see if it is a valid date.'''
import re
from types import NoneType
dateRegex = re.compile(r'^(0?\d{1,2})/(0?\d{1,2})/(\d\d\d\d)$')
get_input = True
while get_input:
    input_date = input('Please enter your birthday in the DD/MM/YYYY format: ')
    mo = dateRegex.search(input_date)
    if mo != None:
        get_input = False
        
day, month, year = (mo.groups())
int_month = int(month)
int_year = int(year)
int_day = int(day)
print(f'Day: {day}')
print(f'Month: {month}')
print(f'Year: {year}')

if (int_year % 400 == 0) or (int_year % 4 == 0 and int_year % 100 != 0):
    leap_year = True
else:
    leap_year = False

feb = [2]
thirties = [4, 6, 9, 11]
the_rest = [1,3,5,7,8,10,12]
if int_year < 1000 or int_year > 2999:
    print('The year entered does not make sense.')
elif int_month > 12:
    print(f'Invalid birthday, there are only 12 months, not {month}.')
elif int_month in thirties and int_day > 30:
        print(f'Invalid birthday, there are only 30 days in your birth month.')
elif int_month in the_rest and int_day > 31:
    print(f'Invalid birthday, there are only 31 days in your birth month.')
elif int_month == 2:
    if leap_year == True:
        if int_day > 29:
            print('Invalid birthday, there are only 29 days in February during a leap year.')
    else:
        if int_day > 28:
            print('Invalid birthday, there are only 28 days in February during a nonleap year.')
else:
    print('Valid date entered!')
    
    







