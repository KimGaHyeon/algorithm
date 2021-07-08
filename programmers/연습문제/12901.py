# https://programmers.co.kr/learn/courses/30/lessons/12901
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

print(getDayName(5,24))