
locs = []

while True:

    line = input()

    if line == "":
        break

    locs.append(tuple(map(int, line.split(","))))


width = 0
height = 0

for loc in locs:
    if loc[0] > width:
        width = loc[0] + 1

    if loc[1] > height:
        height = loc[1] + 1


#data = [[0 for i in range(width)] for j in range(height)]


count = 0

for i in range(width):
    for j in range(height):
        total = 0
        for loc in locs:
            total +=  abs(loc[0] - i) + abs(loc[1] - j)

        if total < 10000:
            count += 1
            

print(count)
        


