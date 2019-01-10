rec = [3, 7]

elf1 = 0

elf2 = 1

end = int(input())

while len(rec) < end + 10:



    new = str(rec[elf1] + rec[elf2])

    for char in new:

        rec.append(int(char))


    elf1 = (elf1 + 1 + rec[elf1]) % len(rec)

    elf2 = (elf2 + 1 + rec[elf2]) % len(rec)

    

ans = rec[end:end + 10]

s = ""

for a in ans:
    s += str(a)

print(s)

    

