def collector(input,output):
    words = dict()
    pos = 1
    with open(input) as f:
        for line in f:
            a = []
            b = line.split()
            for element in range(len(b)):
                for elem in range(len(b[element])):
                    if b[element][elem].isalpha() or b[element][elem] == "-" or b[element][elem] == "'":
                        a.append(b[element][elem].lower())
                for i in range(len(a) - 1,0,-1):
                    if a[i].isalpha():
                        break
                    else:
                        a.pop()
                for i in range(0,len(a) - 1):
                    if a[i] == "'":
                        if i == len(a) - 2:
                            break
                        else:
                            a.pop(i)
                while a[0].isalpha() == False:
                    if a[0] == "-":
                        a.pop(0)
                for i in range(1,len(a) - 1):
                    if a[i] == "-":
                        if not((a[i + 1].isalpha() or a[i+1]=='*') and (a[i - 1].isalpha() or a[i-1]=='*')) :
                            a[i] = "*"
                c = []
                for i in range(len(a)):
                    if a[i] != "*":
                        c.append(a[i])
                if "".join(c) not in words.keys():
                    words["".join(c)] = [pos]
                    pos+=1
                else:
                    words["".join(c)].append(pos)
                    pos+=1











collector("input.txt","output.txt")