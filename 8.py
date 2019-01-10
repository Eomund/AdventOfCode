
class Node:
    
    def __init__(self, rdata):

        self.numc = rdata[0]
        self.numm = rdata[1]

        self.data = rdata[2:]

        self.value = None
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
        self.value = sum(self.data[:self.length - 2][-self.numm:])
        
    def findValue(self):
        v = self.value

        for c in self.children:
            v += c.findValue()

        return v
        

def printLength(n):

    print(n.length)

    for c in n.children:
        printLength(c)

data = list(map(int, input().strip().split(" ")))

root = Node(data)

root.findLength()

print(root.findValue())

