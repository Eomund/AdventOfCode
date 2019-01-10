line = input()


for i in range(len(line) - 1, 0, -1):
    if line[i] != line[i - 1] and line[i].upper() == line[i - 1].upper():
        line = line[:i - 1] + line[i + 1:]
    

print(len(line))
