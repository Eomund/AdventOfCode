
def within(sub, whole):





    for w in range(1 + len(whole) - len(sub)):
        
        count = 0
        bad = False
        while count < len(sub) and w + count < len(whole):

            if sub[count] == whole[w + count]:
                count += 1
            else:
                bad = True
                break

        if not bad:
            return w

    return None
            



rec = [3, 7]

elf1 = 0

elf2 = 1

line = input()

end = []

for c in line:
    end.append(int(c))


pos = None

tested = 0

while True:



    new = str(rec[elf1] + rec[elf2])

    for char in new:

        rec.append(int(char))


    elf1 = (elf1 + 1 + rec[elf1]) % len(rec)

    elf2 = (elf2 + 1 + rec[elf2]) % len(rec)

    pos = within(end, rec[tested - len(end):])
    if not pos == None:
        break
    tested = len(rec)

    
print(tested - len(end) + pos)

    

