from string import ascii_lowercase

def react(line):

    for i in range(len(line) - 1, 0, -1):

        if i >= len(line):
            continue


        if line[i] != line[i - 1] and line[i].upper() == line[i - 1].upper():
            line = line[:i - 1] + line[i + 1:]

    return len(line)


line = input()

lens = []


for let in ascii_lowercase:
    test = line.replace(let, "")
    test = test.replace(let.upper(), "")

    lens.append(react(test))

print(min(lens))
