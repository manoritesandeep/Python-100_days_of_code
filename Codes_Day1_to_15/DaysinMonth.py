"""
In the starting code, you'll find the solution from the Leap Year challenge.
 First, convert this function is_leap() so that instead of printing 
 "Leap year." or "Not leap year." it should return 
  True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() 
    which will take a year and a month as inputs
    use this information to work out the number of days in the month, 
    then return that as the output,
"""

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year.")
        return True
      else:
        # print("Not leap year.")
        return False
    else:
    #   print("Leap year.")
        return True
  else:
    # print("Not leap year.")
    return False

def days_in_month(year:int, month:int):
    if month >12 or month < 1:
       return "Invalid month entered!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        month_days = month_days[1] + 1
        return month_days 
    return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
