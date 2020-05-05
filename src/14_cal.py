"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


def get_calendar(args):
    invalid_input_message = "Please give arguments in script [month 1-12] [year 1970-3000] format."

    # Renders a calendar with optional parameters:
    # {int} - month within the range 1-12
    # {int} - year within the range 1970-3000
    def render_calendar(month=datetime.today().month, year=datetime.today().year):
        print(calendar.month(int(year), int(month)))

    def check_month_input(month_arg):
        if month_arg.isdigit() and 1 <= int(month_arg) <= 12:
            return True

    def check_year_input(year_arg):
        if year_arg.isdigit() and 1970 <= int(year_arg) <= 3000:
            return True

    # A switch function to help render calendar based on how many arguments were passed in
    def switch(args_given):
        if args_given == 1:
            render_calendar()

        elif args_given == 2:
            month = args[1]
            if check_month_input(month):
                render_calendar(month)
            else:
                return invalid_input_message

        elif args_given == 3:
            month = args[1]
            year = args[2]
            if check_month_input(month) and check_year_input(year):
                render_calendar(month, year)
            else:
                return invalid_input_message

        else:
            return invalid_input_message

    return switch(len(args))


print(get_calendar(sys.argv))
