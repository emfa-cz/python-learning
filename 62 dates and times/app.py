import datetime

date = datetime.date(2026, 7, 15)
today = datetime.date.today()
time = datetime.time(12, 30, 52)
now = datetime.datetime.now()
now = now.strftime("%H %M %S - %y %m %d")
targetDateTime = datetime.datetime(2030, 1, 2, 12, 30, 1)
currentDateTime = datetime.datetime.now()

if targetDateTime < currentDateTime:
    print("target date had passed")
else:
    print("target date had not passed")

print(now)