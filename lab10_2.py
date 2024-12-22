import numpy as np

years = np.arange(1900, 2020+5, 1)
def generate_leap_years(years):
    '''
    the function returns a list of leap years from a given list of years.
    '''
    leap_years = list(filter(lambda i: i % 400 == 0 or (i % 100 != 0 and i % 4 == 0), years))
    return leap_years
print('Leap years = ', generate_leap_years(years))  # print the list of leap years

def days_in_month(month, year, generate_leap_years):
    '''
    the function returns the number of days in a given month for a specific year.
    '''
    if month == 2 and year in generate_leap_years(years):  # check if the month is February and if the year is a leap year
        return 29
    elif month == 2:
        return 28
    elif (month < 8 and month % 2 == 1) or (month >= 8 and month % 2 == 0):
        return 31                 # months with 31 days: Jan, Mar, May, Jul, Aug, Oct, Dec
    elif (month < 8 and month % 2 == 0) or (month >= 8 and month % 2 == 1):
        return 30                 # months with 30 days: Apr, Jun, Sep, Nov
    
while True:     # check for a valid month from user                              
    try:                                                 
        while True:
            month = int(input('Enter a month: '))
            if month > 0 and month < 13:
                break
            else:
                print('Enter a value between 1 and 12.')
                continue                                                                                                                     
    except ValueError:  
        print('Error! Enter a valid number.')
        continue
    else:
        break 

while True:     # check for a valid year from user                                     
    try:                                                 
        while True:
            year = int(input('Enter a year: '))
            if year > 1899 and year < 2025:
                break
            else:
                print('Enter a value between 1900 and 2024.')
                continue                                                                                                                     
    except ValueError:  
        print('Error! Enter a valid number.')
        continue
    else:
        break 
# print the number of days in the specific month and year
print(days_in_month(month, year, generate_leap_years), 'days in this month.')