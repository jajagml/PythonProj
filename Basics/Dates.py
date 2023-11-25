# dates - it used datetime built-in module 
from datetime import datetime as dt # in line 2, I applied what I learned from python module feature

today = dt.now() # in line 4, now() method returns the date today
print(today)
print(today.year) # .year returns the today's year
print(today.strftime("%A")) # %A returns the name of day today e.g. Sunday
print(today.strftime("%a")) # %a returns the short name of day today e.g. Sun
date1 =dt(1901, 11, 15)
print(date1) # will return the given parameters into date format yyyy, mm, dd
print(date1.strftime("%B")) # %B returns the name of month from the given date
print(date1.strftime("%A"))
print(date1.strftime("%w")) # %w weekday as a number, where Sunday is 0  
print(date1.strftime("%y")) # %y short year format ex. 2019 = 19
print(date1.strftime("%Y")) # %Y returns the year ex. 2019