def odometer(M):
    lengh = len(M)
    for i in range(0, lengh, 2):
        if i == 0:
            way = M[i] * M[i+1]
        else:
            way += M[i] * (M[i+1] - M[i - 1])
    return way