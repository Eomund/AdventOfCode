

def diff(s1, s2):

    for i in range(len(s1)):

        if s1[:i] + s1[i + 1:] == s2[:i] + s2[i + 1:]:

            return i

    return -1




data = []

while(True):
    line = input()

    if line == "":
        break


    data.append(line)


done = False

for i in range(len(data)):

    for j in range(i + 1, len(data)):

       ans = diff(data[i], data[j])

       if ans != -1:
           done = True
           print(data[i][:ans] + data[i][ans + 1:])
           break

    if done:
        break




        
