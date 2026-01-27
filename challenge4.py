# CHALLENGE #4: Return the number of times a day of the week
# appears in a given month.

import calendar

def count_days(year, month, whichday):
    # The parameter 'whichday' can only be between 0 (Monday)
    # and 6 (Sunday).
##    print(calendar.day_name[whichday])
    counter = 0
    cal = calendar.monthcalendar(year, month)
    for d in range(0,7):
        if d == cal.day_name[whichday]:
            counter = counter+1
    print(counter)

##    if (year%4 == 0): # On leap years, February has 29 days.
##        for d in range(1,29):
            

# EXAMPLE: In December 2025, there are five Mondays.
# Therefore, count_days() should return 5.
test_year = 2025
test_month = 12
test_day = 6
count_days(test_year, test_month, test_day)

