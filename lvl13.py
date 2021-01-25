def MassVote(N, Votes):
    N = N
    Votes = Votes
    max = Votes[0]
    summa = 0
    flag = False
    position = 1
    for i in range(1, len(Votes)):
        if(max < Votes[i]):
            max = Votes[i]
            position = i + 1
    if(Votes.count(max) > 1):
        flag = True
    for i in Votes:
        summa += i
    result = 0

    if(flag == False):
        result = (max * 100) / 100
        if(result > 50):
            string = "majority winner " + str(position)
            return string
        if(result <= 50):
            string = "minority winner " + str(position)
            return string
    else:
        string = "no winner"
        return string
print(MassVote(3, [23, 50, 27]))
