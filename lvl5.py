def MadMax(N, Tele):
    N = len(Tele)
    for i in range(N):
        for j in range(N-i-1):
            if Tele[j] > Tele[j+1]:
                Tele[j], Tele[j+1] = Tele[j+1], Tele[j]
                
    two = Tele[int((N-1)/2) : N]
    two.reverse()
    k = 0
    for j in range(int((N-1)/2), N):
        Tele[j] = two[k]
        k += 1
    return Tele