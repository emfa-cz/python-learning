import threading
import time

def walkDog():
    time.sleep(8)
    print(f"you finihsed walkig the dof {first} {last}")
    

def takeOutTrash():
    time.sleep(2)
    print("you finished taking out the trash")
    

def getMail():
    time.sleep(4)
    print("you get the mail")


chore1 = threading.Thread(target=walkDog, args=("scooby", "doo"))
chore1.start()
chore2 = threading.Thread(target=takeOutTrash)
chore2.start()
chore3 = threading.Thread(target=getMail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("all chores are complete")