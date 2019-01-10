
class Node:
    
    def __init__(self, rdata):

        self.numc = rdata[0]
        self.numm = rdata[1]

        self.data = rdata[2:]

        self.meta = None
        self.length = None


    def findLength(self):

        self.children = [None] * self.numc
        self.length = self.numm + 2

        skip = 0
        
        for i in range(len(self.children)):
            self.children[i] = Node(self.data[skip:])
            self.children[i].findLength()
            self.length += self.children[i].length
            skip += self.children[i].length
        self.meta = self.data[:self.length - 2][-self.numm:]
        
    def findMeta(self):
        m = sum(self.meta)

        for c in self.children:
            m += c.findMeta()

        return m


    def findValue(self):

        if len(self.children) == 0:

            return sum(self.meta)

        val = 0

        for m in self.meta:

            if m - 1 < len(self.children):

                val += self.children[m - 1].findValue()

        return val
        

def printLength(n):

    print(n.length)

    for c in n.children:
        printLength(c)

data = list(map(int, input().strip().split(" ")))

root = Node(data)

root.findLength()

print(root.findValue())

