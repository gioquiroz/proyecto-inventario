from datetime import date,time,datetime
localTime = date.today()
print(localTime)
def fecha(a,m,d):
    print("AA/MM/DD")
    movieDate = date(a,m,d)
    operation =  localTime - movieDate
    return operation
print(fecha(2021,8,22))
