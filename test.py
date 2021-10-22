import csv
import datetime


days = {"Friday":0,"Sunday":2,"Monday":4,"Tuesday":6,"Wednesday":8}

day = datetime.datetime.now().strftime("%A")
currentTime = datetime.datetime.now().strftime("%H:%M")

with open("hour.csv","r") as f:
        r = csv.reader(f)
        times = []
        hours = []
        for i in r:
            times.append(i)
        hours.append(times[days[day]])
        print(hours[0])

def dayCheck():
    return day in days.keys();

if (dayCheck() == True):
    print(3)