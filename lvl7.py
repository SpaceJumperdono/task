def PatternUnlock(N, hits):
    lengh = N
    hits = hits
    a = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    dotes = []
    for i in range(N):
        for j in range(len(a)):
            for k in range(len(a[0])):
                if(hits[i] == a[j][k]):
                    c = str(j) + str(k)
                    dotes.append(c)
    result = 0
    for i in range(len(dotes)-1):
        one_list = dotes[i]
        dote_first_one_one = one_list[:1]
        dote_first_one_two = one_list[1:2] 
        two_list = dotes[i+1]
        dote_second_one_one = two_list[:1]
        dote_second_one_two = two_list[1:2]
        if dote_first_one_one != dote_second_one_one and dote_first_one_two != dote_second_one_two:
            result += 2 ** .5
        else:
            result += 1
    result = str(format(result, '.5f'))
    string = ''
    for i in result:
        if i != '.' and i != '0':
            string = string + i
    return string
print(PatternUnlock(2, [4,2]))