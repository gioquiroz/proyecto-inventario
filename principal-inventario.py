from datetime import date,time,datetime
localTime = date.today()
print(localTime)
movieDate = date(2021, 8, 22)
operation = movieDate - localTime
print(operation)