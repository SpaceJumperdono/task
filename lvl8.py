def score(lis):
    a = lis
    res = ''
    for i in a:
        res = res + ' ' + i
    return int(len(res) - 1)

def stroke(l, string):
    size = l
    string = string
    spisok = string.split(' ')
    print(spisok)
    a = [[]]
    lengh = len(spisok)
    i = 0
    j = 0
    while i < lengh:
        check = score(a[j]) + len(str(spisok[i])) + 1
        if(check <= size):
            a[j].append(spisok[i])
        else:
            j += 1
            a.append([spisok[i]])
        i += 1
    return a

def score_line(lis):
    a = lis
    res = ''
    for i in a:
        res = res + i
    return int(len(res)) 

def linez(size, string):
    size = size
    spisok = string
    a = [[]]
    lengh = len(str(spisok))
    i = 0
    j = 0
    while i < lengh:
        check = score_line(a[j]) + len(spisok[i])
        if(check <= size):
            a[j].append(spisok[i])
        else:
            j += 1
            a.append([spisok[i]])
        i += 1
    return a

def WordSearch(len, s, subs):
    if(' ' in s):
        spisok = stroke(len, s)
        line = []
        for i in spisok:
            b = ''.join(i)
            if(subs in i):
                line.append(1)
            else:
                line.append(0)
        return line
    else:
        spisok = linez(len, s)
        line = []
        for i in spisok:
            b = ''.join(i)
            if(subs in b):
                line.append(1)
            else:
                line.append(0)
        return line