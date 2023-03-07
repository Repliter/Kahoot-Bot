# tutorial > https://youtu.be/otumBF39v3o 
from kahoot import client
import random
import os
import threading

bot = client()
print("emppu.cc")
gameid = input(f"Game Pin: ")
custom_usr = input("Bot names: ")
custom_usr = custom_usr+" - "
threadamount = 200
bots = 1;
print()
os.system("clear")
def liity():
    bots = 1;
    usrname = (custom_usr + str(random.randint(1, 100000)))
    bot.join((gameid), usrname)
    def joinHandle() :
            pass
    bot.on("joined", joinHandle)
    print (f"{usrname} joined")
    bots += 1
    while True:
        liity()

threadamount = int(threadamount)
for x in range(threadamount):
    t1 = threading.Thread(target=liity)
    t1.start()
