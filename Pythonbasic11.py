from calendar import calendar


#printing a calendar from calendar module
import calendar
yy=int(input("Enter the year of the calendar: "))
mm=int(input("Enter the month of the calendar: "))
a=calendar.month(yy,mm)
print(a)