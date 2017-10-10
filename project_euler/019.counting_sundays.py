'''
Problem 019

You are given the following information, but you may prefer to do some research
    for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century 
   unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century 
   (1 Jan 1901 to 31 Dec 2000)?


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
class year_365():
    start_dates  = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

    def __init__(self):
        self.start_dates

    def get_dates(self):
        return self.start_dates


class year_366():
    start_dates  = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]

    def __init__(self):
        self.start_dates

    def get_dates(self):
        return self.start_dates


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True

    return False


def get_sundays(first_sunday, is_leap):
    sundays = []
    sunday_count = 0
    for day in range(first_sunday, 337, 7):
        sundays.append(day)
    
    if is_leap:
        first_dates = year_366()
    else:
        first_dates = year_365()

    for day in sundays:
        if day in first_dates.get_dates():
            sunday_count += 1

    return sunday_count


def solve_problem():
    count = 0
    sunday_cycle = 6   # First Sunday in 1901
    
    for year in range(1901, 2001):
        if sunday_cycle == 0:
            sunday_cycle = 7
        if is_leap_year(year):
            count += get_sundays(sunday_cycle, True)
            sunday_cycle -= 2
        else:
            count += get_sundays(sunday_cycle, False)
            sunday_cycle -= 1

    return(count)


if __name__ == "__main__":
    print(solve_problem())
