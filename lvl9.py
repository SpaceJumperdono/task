def copy(L):
    l = []
    for i in L:
        l.append(i)
    return l

def SumOfThe(N, data):
    lengh = N
    a = data
    for i in range(len(a)):
        cop = copy(a)
        cop[i] = 0
        res = 0
        for j in range(len(a)):
            res += cop[j]
        if(a[i] == res):
            return a[i]