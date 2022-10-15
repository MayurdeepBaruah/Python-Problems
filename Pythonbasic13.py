#calculating days in between dates 
from datetime import date
d1=date(2022,10,1)
d2=date(2022,10,13)
d3=d2-d1
print(d3.days)