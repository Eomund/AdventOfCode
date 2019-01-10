plants = []
offset = 0


def convert(s):

    l = []
    for char in s:

        if char == "#":
            l.append(True)

        if char == ".":
            l.append(False)

    return l

births = []
deaths = []


line = input().split(": ")[1]

plants = convert(line)

while plants[0] or plants[1] or plants[2]:

    plants.insert(0, False)

    offset -= 1

while plants[-1] or plants[-2] or plants[-3]:
    plants.append(False)




input()

while True:

    line = input()

    if line == "":
        break

    parts = line.split(" => ")
    
    if parts[1] == "#":


        births.append(convert(parts[0]))

    if parts[1] == ".":

        deaths.append(convert(parts[0]))

prnt = ""
for p in plants:
    if p:
        prnt += "#"
    else:
        prnt += "."
print(prnt)

points = []

for gen in range(1000):



    while plants[0] or plants[1] or plants[2] or plants[3] or plants[4]:
        #print(plants[0], plants[1], plants[2], plants[3], plants[4])
        plants.insert(0, False)

        offset -= 1

    while plants[-1] or plants[-2] or plants[-3] or plants[-4] or plants[-5]:
        #print(plants[-1], plants[-2], plants[-3], plants[-4], plants[-5])
        plants.append(False)

    nxtgen = [False] * len(plants)

    for p in range(len(plants) - 5):
        for b in births:
            if plants[p:p + 5] == b:

                nxtgen[p + 2] = True

        for d in deaths:
            if plants[p:p + 5] == d:

                nxtgen[p + 2] = False

                
    plants = nxtgen.copy()


##    prnt = str(gen + 1) + ": "
##    for p in plants:
##        if p:
##            prnt += "#"
##        else:
##            prnt += "."


    total = 0

    for i in range(len(plants)):

        if plants[i]:
            total += i + offset

    points.append([gen + 1, total])


m = (points[-1][1] - points[500][1]) / (points[-1][0] - points[500][0])



b = points[500][1] - m * points[500][0]

print("y = ", m, " x + ", b)

print(m * 50000000000 + b)


