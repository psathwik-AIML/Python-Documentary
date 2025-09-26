# used for date and time 
import datetime 
now =datetime.datetime.now()
print(now)
# date 
print(now.date())
# time
print(now.time())
# month 
print(now.month)
# date 
print( now.day)
# year 
print(now.year)
# own  date 
print(now.strftime("31-03-2003"))
# own time 
print(now.strftime("11:8:55"))