

class Step:

    def __init__(self, n):

        self.name = n

        self.children = []
        self.parents = []

    def addChild(self, c):

     
        self.children.append(c)

    def addParent(self, p):

        self.parents.append(p)

    def __repr__(self):

        return self.name

    def __str__(self):

        return self.name
        

steps = []

while True:

    line = input()

    if line == "":

        break

    before = line[5]
    after = line[36]
    apos = None

    for i in range(len(steps)):
        if steps[i].name == after:
            apos = i
            break

    if apos == None:
        apos = len(steps)
        steps.append(Step(after))

    found = False
    for s in steps:
        if s.name == before:
            s.addChild(steps[apos])
            steps[apos].addParent(s)
            found = True
            break

    if not found:
        newStep = Step(before)
        newStep.addChild(steps[apos])
        steps[apos].addParent(newStep)
        steps.append(newStep)

    



avail = []

for s in steps:
    if len(s.parents) == 0:
        avail.append(s)

done = []
ans = ""
while len(avail) > 0:


    
    curPos = 0
    curName = avail[0].name
    for i in range(1, len(avail)):
        if avail[i].name < curName:
            curName = avail[i].name
            curPos = i

    ans += avail[curPos].name

    done.append(avail[curPos])

    for c in avail[curPos].children:

        good = True
        
        for p in c.parents:
    
            if not p in done:
                good = False
                break
        if good:
            avail.append(c)

    del avail[curPos]

print(ans)
