# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year must be evenly divisible by 4.
# If the year is also evenly divisible by 100, it is NOT a leap year......
# UNLESS the year is also evenly divisible by 400, which makes it a leap year again



def is_leap(year):
    leap = False

    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap= True
        else :
            leap=True
        
    return leap
year = int(input())
print(is_leap(year))\
    
# logic

# i first check weather the year is divisible by 4
# if it is then i check if year is divisible by 100 if yes then check by dividing 400
# if year is not divisible by 100 then we know year is leap then we just print the else condition

