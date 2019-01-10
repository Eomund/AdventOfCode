

twos = 0
threes = 0

while(True):
    line = input()

    if line == "":
        break

    counts = {}

    for let in line:
        if let in counts:

            counts[let] += 1

        else:

            counts[let] = 1


    for c in counts.values():

        if c == 2:
            twos += 1
            break

    for c in counts.values():

        if c == 3:
            threes += 1
            break


print(twos * threes)
