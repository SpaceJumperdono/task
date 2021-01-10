def score(lis):
    a = lis
    res = ''
    for i in a:
        res = res + ' ' + i
    return int(len(res) - 1) 
def stroke(l, string):
    lengh = l
    string = string
    spisok = string.split(' ')
    print(spisok)
    a = [[]]
    lengh = len(spisok)
    i = 0
    j = 0
    while i < lengh:
        example = a[j]
        check = score(a[j]) + len(str(spisok[i])) + 1
        if(check <= 12):
            a[j].append(spisok[i])
        else:
            j += 1
            a.append([spisok[i]])
        i += 1
    return a
def WordSearch(len, s, subs):
    spisok = stroke(len, s)
    line = []
    for i in spisok:
        if(subs in i):
            line.append(1)
        else:
            line.append(0)
    return line      
    