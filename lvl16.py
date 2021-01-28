def get_list(H, W, string):
    string = string.replace(' ', '')
    map_ = []
    i = 0
    while i < len(string):
        for j in range(H):
            map_.append([])
            for k in range(W):
                map_[j].append(string[i])
                i += 1
    return map_


def TankRush(H1, W1, S1, H2, W2, S2):
    string1 = get_list(H1, W1, S1)
    string2 = get_list(H2, W2, S2)

    for i in range(len(string1)):
        if (len(string2) > 0):
            for j in range(len(string2)):
                if (set(string2[j]).issubset(string1[i])):
                    del string2[j]
                    break
    if (string2):
        return False
    else:
        return True
