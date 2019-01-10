
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


data = [[None for i in range(width)] for j in range(height)]



for i in range(width):
    for j in range(height):
        dist = []

        for loc in locs:
            dist.append(abs(loc[0] - i) + abs(loc[1] - j))
        small = min(dist)
        pos = dist.index(small)
        unique = True
        for d in range(len(dist)):
            if dist[d] == small and pos != d:
                unique = False
                break

        if unique:
            data[j][i] = pos

counts = [0] * len(locs)
inf = [False] * len(locs)

for i in range(width):
    for j in range(height):
        if data[j][i] != None:
            counts[data[j][i]] += 1

for i in range(width):
    if data[0][i] != None:
        inf[data[0][i]] = True
    if data[-1][i] != None:
        inf[data[-1][i]] = True

        
for j in range(height):
    if data[j][0] != None:
        inf[data[j][0]] = True
    if data[j][-1] != None:
        inf[data[j][-1]] = True

for i in range(len(counts) - 1, -1, -1):
    if inf[i]:
        del counts[i]

print(max(counts))
