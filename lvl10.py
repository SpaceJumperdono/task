flag = True
a = 'ирпщие сиоедй тяхне ооиит'
if(flag == True):
    lengh = len(a.replace(' ', ''))
    string = [[]]
    j = 0
    y = 1
    for i in a:
        if(i == ' '):
            string.append([])
            j += 1
            y += 1
        if(i != ' '):
            string[j].append(i)
    print(string)
    min = len(string[0])
    max = len(string[0])
    for i in range(len(string)):
        if max <= len(string[i]):
            max = len(string[i])
        if min >= len(string[i]):
            min = len(string[i])
    print(max, min)
    line = []
    for i in range(max):
        for j in range(y):
            if(i <= max and lengh > 0):
                line.append(string[j][i])
                lengh -= 1
    print(line)
    
    
    
    
    
    
    
    
    
    
if(flag == False):
    a = a.replace(' ', '')
    lengh = len(a)
    sqrt = str(lengh ** 0.5)
    x = int(sqrt[0:1])
    y = int(sqrt[2:3])
    if(x*y < lengh):
        x += 1
    spisok = []
    for i in range(y):
        spisok.append([])
    print(a)
    print(spisok)
    j = 0
    k = 0
    for i in range(lengh):
        if (j >= x):
            j = 0
            k += 1
        spisok[k].append(a[i])
        j += 1
    print(spisok)
    string = []
    for i in range(x):
        for j in range(y):
            if i < len(spisok[j]):
                string.append(spisok[j][i])
        string.append(' ')
    result = ''.join(string)
    print(result)



