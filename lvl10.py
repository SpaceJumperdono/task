def TheRabbitsFoot(s, encode):
    a = s
    flag = encode
    if(flag == False):
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
        min = len(string[0])
        max = len(string[0])
        for i in range(len(string)):
            if max <= len(string[i]):
                max = len(string[i])
            if min >= len(string[i]):
                min = len(string[i])
        line = []
        for i in range(max):
            for j in range(y):
                if(lengh > 0):
                    line.append(string[j][i])
                    lengh -= 1
        result = ''.join(line)
        return result
    if(flag == True):
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
        j = 0
        k = 0
        for i in range(lengh):
            if (j >= x):
                j = 0
                k += 1
            spisok[k].append(a[i])
            j += 1
        string = []
        for i in range(x):
            for j in range(y):
                if i < len(spisok[j]):
                    string.append(spisok[j][i])
                    if(lengh > 0):
                        lengh -= 1
            if(lengh > 0):
                string.append(' ')
        result = ''.join(string)
        return result