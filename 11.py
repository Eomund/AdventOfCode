gsn = 18
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
        row.append(num - 5)


    cells.append(row)

highest = 0
highpos = []



for size in range(1, 300):
    for y in range(301 - size):

        for x in range(301 - size):

            total = 0

            

            if total > highest:
                highest = total
                highpos = [x + 1, y + 1, size]

print(highest, highpos)
