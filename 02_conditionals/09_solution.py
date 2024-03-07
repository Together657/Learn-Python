year = 2023

#   if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        leap_year = True
    else:
        leap_year = False
else:
    leap_year = False

print(f"Is {year} a leap year? {'Yes' if leap_year else 'No'}")