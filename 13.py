from enum import Enum
from operator import attrgetter

class Dir(Enum):

    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3





class Cart:

    def __init__(self, x, y, d):

        self.x = x
        self.y = y
        self.dir = d

        self.turn = 0


    def move(self):

        #print(self.x, self.y, self.dir, track[self.y][self.x])


        
        if self.dir == Dir.NORTH:
            self.y -= 1
            if track[self.y][self.x] == "/":
                self.dir = Dir.EAST
            elif track[self.y][self.x] == "\\":
                self.dir = Dir.WEST
            elif track[self.y][self.x] == "+":
                if self.turn == 0: 
                    self.dir = Dir.WEST
                elif self.turn == 2:
                    self.dir = Dir.EAST
                self.turn = (self.turn + 1) % 3

        elif self.dir == Dir.SOUTH:
            self.y += 1
            if track[self.y][self.x] == "/":
                self.dir = Dir.WEST
            elif track[self.y][self.x] == "\\":
                self.dir = Dir.EAST
            elif track[self.y][self.x] == "+":
                if self.turn == 0: 
                    self.dir = Dir.EAST
                elif self.turn == 2:
                    self.dir = Dir.WEST
                self.turn = (self.turn + 1) % 3
                
        elif self.dir == Dir.WEST:
            self.x -= 1
            if track[self.y][self.x] == "/":
                self.dir = Dir.SOUTH
            elif track[self.y][self.x] == "\\":
                self.dir = Dir.NORTH
            elif track[self.y][self.x] == "+":
                if self.turn == 0: 
                    self.dir = Dir.SOUTH
                elif self.turn == 2:
                    self.dir = Dir.NORTH
                self.turn = (self.turn + 1) % 3
                
        elif self.dir == Dir.EAST:
            self.x += 1
            if track[self.y][self.x] == "/":
                self.dir = Dir.NORTH
            elif track[self.y][self.x] == "\\":
                self.dir = Dir.SOUTH
            elif track[self.y][self.x] == "+":
                if self.turn == 0: 
                    self.dir = Dir.NORTH
                elif self.turn == 2:
                    self.dir = Dir.SOUTH
                self.turn = (self.turn + 1) % 3

        #print(self.x, self.y, self.dir, track[self.y][self.x])



        for c in carts:

            if not self == c and self.x == c.x and self.y == c.y:
                return c

        return None
            
track = []
carts = []
y = 0



while True:

    line = input()

    if line == "":
        break

    row = []

    for x in range(len(line)):

        if line[x] == ">":

            carts.append(Cart(x, y, Dir.EAST))

            row.append("-")

        elif line[x] == "<":

            carts.append(Cart(x, y, Dir.WEST))

            row.append("-")

        elif line[x] == "^":

            carts.append(Cart(x, y, Dir.NORTH))

            row.append("|")
            
        elif line[x] == "v":

            carts.append(Cart(x, y, Dir.SOUTH))

            row.append("|")

        else:

            row.append(line[x])

    track.append(row)
    y += 1
    




while True:

    carts.sort(key=attrgetter('x'))
    carts.sort(key=attrgetter('y'))

    crash = False
    remove = []
    for c in carts:
        crashCart = c.move() 
        if not crashCart == None:
            remove.append(c)
            remove.append(crashCart)

    for r in remove:
        carts.remove(r)


    if len(carts) == 1:
        break
        
            
print(carts[0].x, carts[0].y)
