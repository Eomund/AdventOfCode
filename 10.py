import time

lights = []

mxvelx = 0
mxvely = 0

while True:

    line = input()

    if line == "":

        break
    
    parts = line.split("<")

    posParts = parts[1].split(",")

    
    pos = [int(posParts[0].strip()), int(posParts[1].split(">")[0].strip())]

    velParts = parts[2].split(",")
    
    vel = [int(velParts[0].strip()), int(velParts[1].split(">")[0].strip())]

    if abs(vel[0]) > mxvelx:
        mxvelx = abs(vel[0])

    if abs(vel[1]) > mxvely:
        mxvely = abs(vel[1])

    lights.append([pos, vel])

prevH = 1000000
prevW = 1000000


count = 0
while True:
    count += 1
    maxx = lights[0][0][0]
    maxy = lights[0][0][1]
    minx = lights[0][0][0]
    miny = lights[0][0][1]


    
    for l in lights:
        if l[0][0] > maxx:
            maxx = l[0][0]
        if l[0][1] > maxy:
            maxy = l[0][1]

        if l[0][0] < minx:
            minx = l[0][0]
        if l[0][1] < miny:
            miny = l[0][1]



    width = maxx - minx + mxvelx
    height = maxy - miny + mxvely

    if width > prevW and height > prevH:
        break

    for l in lights:


        l[0][0] += l[1][0]
        l[0][1] += l[1][1]

    prevW = width
    prevH = height

pic = [None] * height

for i in range(len(pic)):
    pic[i] = ["."] * width

for l in lights:
    l[0][0] -= l[1][0]
    l[0][1] -= l[1][1]
    pic[l[0][1] - miny][l[0][0] - minx] = "#"

print(count - 2)

for row in pic:
    st = ""
    for el in row:
        st += el
    print(st)
