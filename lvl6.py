def copy(L):
    l = []
    for i in L:
        l.append(i)
    return l
    
def sort(N, L):
    for i in range(N):
        for j in range(N-i-1):
            if(L[j] > L[j+1]):
                L[j], L[j+1] = L[j+1], L[j]
    return L

def SynchronizingTables(N, ids, salary):
    N = N
    copy_ids = copy(ids)
    copy_ids = sort(N, copy_ids)
    index_ids = []
    for i in range(N):
        for j in range(N):
            if(copy_ids[j] == ids[i]):
                index_ids.append(j)
                continue
    
    copy_salary = copy(salary)
    copy_salary = sort(N, copy_salary)
    
    for m in range(N):
        for k in range(N):
            if(index_ids[k] == m):
                salary[k] = copy_salary[m]
                break
    return salary