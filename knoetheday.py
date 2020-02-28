#This program will take input in the form (date month year) separated by space and tell which day was on this date.
import calendar as c #importing an module calendar

def day(num):               #defining a method day which will take paremeter as a number returned from tell function in the program
    if num==0:
        return 'MONDAY'
    elif num==1:
        return 'TUESDAY'
    elif num==2:
        return 'WEDNESDAY'
    elif num==3:
        return 'THURSDAY'
    elif num==4:
        return 'FRIDAY'
    elif num==5:
        return 'SATURDAY'
    elif num==6:
        return 'SUNDAY'
    
def tell(year,mon,date):   #defining a method that takes input parameters as year month and date
    t=c.weekday(int(year),int(mon),int(date))   #Here we are changing the type of year,month,dare as integer
    r=day(t)
    return r
    
d=input('Enter the date:\n')


e=d.split(' ')
w=tell(e[-1],e[1],e[0])
print('On',d,'the day was/is,w)



