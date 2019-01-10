from enum import Enum
from datetime import datetime


class Action(Enum):

    START = 0
    WAKE = 1
    SLEEP = 2


class Event:

    def __init__(self, data):

        self.slps = [0] * 60        

        self.ts = datetime.strptime(data[0], "%Y-%m-%d %H:%M")

        self.id = None

        if data[1] == "falls asleep":
            self.act = Action.SLEEP

        elif data[1] == "wakes up":
            self.act = Action.WAKE

        else:

            self.act = Action.START
            self.id = int(data[1].split("#")[1].split(" b")[0])



events = []
slps = {}




while True:

    line = input()

    if line == "":
        break


    events.append(Event(line[1:].split("] ")))

events.sort(key = lambda e:e.ts)

sleeps = {}

active = None
start = None

ids = []

for e in events:
    if e.id != None and e.id not in ids:
        ids.append(e.id)
        slps[e.id] = [0] * 60

for e in events:

    if e.act == Action.START:
        
        active = e.id



    elif e.act == Action.SLEEP:

        start = e.ts

    elif e.act == Action.WAKE:
 
        for i in range(start.minute, e.ts.minute):
            
            slps[active][i] += 1


        if active in sleeps:

            sleeps[active] += e.ts.minute - start.minute

        else:

            sleeps[active] = e.ts.minute - start.minute

long = 0
lid = None

for s in sleeps:
    if sleeps[s] > long:
        lid = s
        long = sleeps[s]





when = None



for anid in ids:

    if anid == lid:
        targ = 0
        ttime = None

        for s in range(len(slps[anid])):
            if slps[anid][s] > targ:
                ttime = s
                targ = slps[anid][s]


        print(lid * ttime)
        break


