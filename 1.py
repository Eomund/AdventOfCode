

s = 0

prev = [0]

while(True):
    data = input()

    if(data == ""):
        break

    s+= int(data)

    print(s)

    if(s in prev):
        print(prev)
        break

    prev.append(s)

print(s)
