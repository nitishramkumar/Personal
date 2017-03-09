N = int(input())
l = []
for i in range(0,N):
    line = input()
    lineVal = line.split()
    if lineVal[0] == "insert":
        val = int(lineVal[2])
        pos = int(lineVal[1])
        l.insert(pos,val)
    elif lineVal[0] == "print":
        print(l)
    elif lineVal[0] == "remove":
        l.remove(int(lineVal[1]))
    elif lineVal[0] == "append":
        l.append(int(lineVal[1]))
    elif lineVal[0] == "sort":
        l.sort()
    elif lineVal[0] == "pop":
        l.pop()
    elif lineVal[0] == "reverse":
        l.reverse()
