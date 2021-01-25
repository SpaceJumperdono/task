def UFO(N, data, octal):
    N = N
    data = data
    octal = octal
    result = 0
    lis = []
    for i in data:
        number = str(i)
        number = number[::-1]
        for j in range(len(number)):
            if(octal == True):
                result += int(number[j]) * (8 ** j)
            else:
                result += int(number[j]) * (16 ** j)
        lis.append(result)
        result = 0
    return lis
