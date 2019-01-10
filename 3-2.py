grid = []

ids = []

for i in range(1000):
    grid.append([])
    for j in range(1000):
        grid[i].append([])

while(True):

    line = input()

    if line == "":
        break


    line = line.split("#")[1]
    parts = line.split("@")

    sid = parts[0].strip()

    ids.append(sid)

    parts = parts[1].split(":")

    loc = parts[0].split(",")

    size = parts[1].split("x")

    loc[0] = int(loc[0])
    loc[1] = int(loc[1])

    size[0] = int(size[0])
    size[1] = int(size[1])

    for i in range(loc[0], loc[0] + size[0]):
        for j in range(loc[1], loc[1] + size[1]):
            grid[i][j].append(sid)

bad = []

for row in grid:
    for el in row:
        if len(el) > 1:
            for shape in el:
                if not shape in bad:
                    bad.append(shape)

for sid in ids:
    if not sid in bad:
        print(sid)
        break

    
