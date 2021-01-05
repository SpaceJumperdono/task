def create_matrix(N, M):
    return [[False] * M for i in range(N)]

def parse_list(L, battalion):
    a = []
    for i in range(L):
        a.append([])
    k = 0
    m = 0
    for j in battalion:
        if(m == 2):
            k += 1
            m = 0
        a[k].append(j-1)
        m += 1
    return a

def get_all_neigborhoods(x, y, matrix, N, M, ready_solder):
    neigborhoods = []
    if (x - 1 >= 0) and (matrix[x-1][y] == False) and ([x-1, y] not in ready_solder):
        neigborhoods.append([x-1, y])
    if (x + 1 < N) and (matrix[x+1][y] == False) and ([x+1, y] not in ready_solder):
        neigborhoods.append([x+1, y])
    if (y - 1 >= 0) and (matrix[x][y-1] == False) and ([x, y-1] not in ready_solder):
        neigborhoods.append([x, y-1])
    if (y + 1 < M) and (matrix[x][y+1] == False) and ([x, y+1] not in ready_solder):
        neigborhoods.append([x, y+1])
   
    return neigborhoods

def ConquestCampaign(N, M, L, battalion):
    matrix = create_matrix(N, M)
    ready_solder = parse_list(L, battalion)
    cnt = 0
    neigborhoods = ready_solder
    while neigborhoods:
        neigborhoods = []
        for solder in ready_solder:
            x = solder[0]
            y = solder[1]
            matrix[x][y] = True
            neigborhoods += get_all_neigborhoods(x, y, matrix, N, M, ready_solder)
        cnt += 1
        if neigborhoods:
            ready_solder = neigborhoods
        else:
            return cnt
        