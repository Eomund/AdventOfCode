gsn = 6392
cells = []

def getCell(x, y):

    global cells

    return cells[y - 1][x - 1]


for y in range(300):

    row = []

    for x in range(300):

        rackid = (x + 11)
        power = rackid * (y + 1)

        num = (((power + gsn) * rackid) // 100) % 10
        row.append([num - 5])


    cells.append(row)

highest = 0
highpos = []



for size in range(1, 300):

    print(size)

    for y in range(301 - size):

        for x in range(301 - size):

            total = cells[y][x][-1]
            for i in range(size):
                total += cells[y + size - 1][x + i][0]
                total += cells[y + i][x + size - 1][0]

            if total > highest:
                highest = total
                highpos = [x + 1, y + 1, size]

            cells[y][x].append(total)

print(highest, highpos)
