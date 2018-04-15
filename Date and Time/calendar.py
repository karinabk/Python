'''Task
You are given a date. Your task is to find what the day is on that date.'''


import calendar
N = list(map(int,input().split()))

if calendar.weekday(N[2],N[0],N[1])==0:
    print('MONDAY')
if calendar.weekday(N[2],N[0],N[1])==1:
    print('TUESDAY')
if calendar.weekday(N[2],N[0],N[1])==2:
    print('WEDNESDAY')
if calendar.weekday(N[2],N[0],N[1])==3:
    print('THURSDAY')
if calendar.weekday(N[2],N[0],N[1])==4:
    print('FRIDAY')
if calendar.weekday(N[2],N[0],N[1])==5:
    print('SATURDAY')
if calendar.weekday(N[2],N[0],N[1])==6:
    print('SUNDAY')
