numPlayers = 465

lastMarble = 7149800

curPos = 0

marbles = [0]

score = [0] * numPlayers

turn = 0

for m in range(1, lastMarble + 1):

    if m % 23 == 0:


        score[turn] += m
        curPos = curPos - 7
        
        curPos = curPos % len(marbles)

        score[turn] += marbles[curPos]
        del marbles[curPos]

    else:
        curPos += 1
        curPos = (curPos % len(marbles)) + 1

        marbles.insert(curPos, m)

    
    turn += 1
    turn = turn % numPlayers


print(max(score))
