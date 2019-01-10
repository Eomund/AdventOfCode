

s = 0

prev = [0]

nums = []

while(True):
    data = input()

    if(data == ""):
        break

    nums.append(int(data))
    

while(True):

    done = False


    for n in nums:

        s += n


      

        if s in prev:
            done = True
            print(s)
            break

        prev.append(s)

    

    if done:
        break
