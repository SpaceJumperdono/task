def check(time, track):
    time = time
    a = track
    line = []
    for i in range(1, time+1):
        line.append(i)
    spisok = []
    i = 0
    case = True
    number = 0
    while i < time:
        if(case == True and i < time):
            spisok.append([])
            for j in range(a[1]):
                if(i < time):
                    spisok[number].append(int(line[i]))
                    i += 1
                else:
                    return spisok
        if(case == False and i < time):
            spisok.append([])
            for j in range(a[2]):
                if(i < time):
                    spisok[number].append(int(line[i]))
                    i += 1
                else:
                    return spisok
        number += 1
        case = not case
        if(i > time):
            return spisok
    return spisok
    
def time_stop(time, track):
    time = time
    a = track
    line = check(time, track)
    print(line)
    position_spisok = 0
    position_element = 0
    time_stop = 0
    for i in range(len(line)):
        if(a[0] in line[i]):
            position_spisok = i
            for j in range(len(line[i])):
                position_element = j
    if(position_spisok%2 != 0):
        time_stop = 0
    else:
        time_stop = a[1] - (position_element+1)
    return time_stop

def Unmanned(L, N, track):
    lengh = L
    number = N
    t = track
    time = 0
    if(lengh > t[0][0]):
        if(len(t) > 1):
            for i in range(len(t)):
                if(i == 0):
                    time = t[i][0] + time_stop(t[i][0], t[i]) + (t[i+1][0] - t[i][0])
                elif(i != 0 and i < number - 1):
                    time += time_stop(time, t[i]) + (t[i+1][0] - t[i-1][0])
            time += lengh - t[number - 1][0]
            return time
        else:
            time = t[0][0] + time_stop(t[0][0], t[0]) + (lengh - t[0][0])
            return time
    else:
        return lengh
