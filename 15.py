from operator import attrgetter, itemgetter



class Unit:

    def __init__(self, e, x, y):

        self.hp = 200
        self.pow = 3

        self.elf = e

        self.x = x
        self.y = y
        self.dist = [None] * len(grid)
        for r in self.dist:
            r = [None] * len(grid[0])

        self.fr = [None] * len(grid)
        for r in self.fr:
            r = [None] * len(grid[0])


    def __repr__(self):
        return str(self)
    
    def __str__(self):

        s = "GOBLIN: "

        if self.elf:
            s = "ELF: "

        s += str(self.x) + ":" + str(self.y) + " : HP:" + str(self.hp)
        
        return s

    def willMove(self):

 
        
        for u in units:
            if not u.isDead() and u.elf != self.elf and ((abs(u.x - self.x) == 1 and u.y == self.y) or (u.x == self.x and abs(u.y - self.y) == 1)):
                return False
        return True




    def walkFrom(self, x, y, fx, fy, d):


        

        if self.dist[y][x] != None and d >= self.dist[y][x]:
            return



        if grid[y][x] == "#":
            self.fr[y][x] = None
            return

        for u in units:
            if self != u and x == u.x and y == u.y:
                self.fr[y][x] = None
                return


        self.dist[y][x] = d

        self.fr[y][x] = [fx, fy]

        self.walkFrom(x, y - 1, x, y, d + 1)
        self.walkFrom(x - 1, y, x, y, d + 1)
        self.walkFrom(x + 1, y, x, y, d + 1)
        self.walkFrom(x, y + 1, x, y, d + 1)
        
        

    def move(self):

        self.dist = [0] * len(grid)
        for i in range(len(self.dist)):
            self.dist[i] = [None] * len(grid[0])
        
        self.fr = [0] * len(grid)
        for i in range(len(self.fr)):
            self.fr[i] = [None] * len(grid[0])
        self.walkFrom(self.x, self.y, -1, -1, 0)
        targets = []

        for t in units:
            if t.elf != self.elf:

                for i in [-1, 1]:
                    
                    if self.dist[t.y][t.x + i] != None:
                        targets.append([t.x + i, t.y, self.dist[t.y][t.x + i]])

                    if self.dist[t.y + i][t.x] != None:
                        targets.append([t.x, t.y + i, self.dist[t.y + i][t.x]])


            
        bad = []
        for t in targets:
            if t[2] == None:
                bad.append(t)

        for b in bad:
            targets.remove(b)



        if len(targets) > 0:
        
            targets.sort(key = itemgetter(0))
            targets.sort(key = itemgetter(1))
            targets.sort(key = itemgetter(2))
            loc = self.fr[targets[0][1]][targets[0][0]]
            prevLoc = [targets[0][0], targets[0][1]]

            while loc[0] != self.x or loc[1] != self.y:
                prevLoc = loc.copy()
                if self.fr[loc[1]][loc[0]] == None:
                    break
                loc = self.fr[loc[1]][loc[0]].copy()

            self.x = prevLoc[0]
            self.y = prevLoc[1]


    def chooseTarget(self):

        targets = []

        for u in units:

            if not u.isDead() and self.elf != u.elf and ((abs(u.x - self.x) == 1 and u.y == self.y) or (u.x == self.x and abs(u.y - self.y) == 1)):
                targets.append(u)

        
        targets.sort(key = attrgetter('hp'))

        if len(targets) > 0:
            return targets[0]

        return None
        

    def attack(self, target):

        target.hp -= self.pow

    def isDead(self):

        return self.hp <= 0

grid = []

units = []

elves = False
gobs = False

r = 0

while True:

    line = input()

    if line == "":
        break

    row = []

    for c in range(len(line)):

        if line[c] == "E":

            row.append(".")
            units.append(Unit(True, c, r))
            elves = True

        elif line[c] == "G":

            row.append(".")
            units.append(Unit(False, c, r))
            gobs = True
        else:

            row.append(line[c])

    grid.append(row)
    r += 1

rounds = 0
while elves and gobs:

    print(rounds)
    print("X" + str(len(units)) + "X")
##    
##    print("XXXXXXXXXXXXXXXXXXXXXXXX")
##    print("ROUND: " + str(rounds))
##    for u in units:
##        print(u)
##
##    print("XXXXXXXXXXXXXXXXXXXXXXXX")

    units.sort(key = attrgetter('x'))
    units.sort(key = attrgetter('y'))
    dead = []
    for u in units:
        if not u in dead:

            
            if u.willMove():
                u.move()


            target = u.chooseTarget()

            if target != None:
                u.attack(target)

                if target.isDead():

                    dead.append(target)


    for d in dead:
        units.remove(d)

    elves = False
    gobs = False

    for u in units:

        
        
        if u.elf:
            elves = True
        else:
            gobs = True

        if elves and gobs:
            rounds += 1
            break

    



hps = 0
for u in units:

#    print(u)
    
    hps += u.hp
#print(hps)
#print(rounds)
print(rounds * hps)

    
