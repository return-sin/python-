months = (31,28,31,30,31,30,31,31,30,31,30,31)
rmonths = (31,29,31,30,31,30,31,31,30,31,30,31)

def Year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def Sum(year,month,day):
    if Year(year):
        return sum(rmonths[:month-1])+day
    else:
        return sum(months[:month-1])+day
    
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
print(Sum(year,month,day))

