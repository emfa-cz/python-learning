import time

my_time = int(input("enter your time: "))

for x in range(my_time, 0, -1):
    secs = x % 60
    minu = int(x / 60) % 60
    hrs = int(x / 3600)
    print(f"{hrs:02}:{minu:02}:{secs:02}")
    time.sleep(1)
