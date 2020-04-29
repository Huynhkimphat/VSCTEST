
# calendar
# import calendar
import datetime
import time
print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 4))
print()

print(calendar.monthcalendar(2020, 4))

print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020, 4, 25)
print()
print(day_of_the_week)


is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2099, 2105)
print(how_many_leap_days)
