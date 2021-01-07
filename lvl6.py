def copy(L):

    l = []
    for i in L:
        l.append(i)
    return l
    
def sort(N, L):
    
    for i in range(N):
        for j in range(N-i-1):
            if(L[j] >= L[j+1]):
                L[j], L[j+1] = L[j+1], L[j]
    return L


def SynchronizingTables(N, ids, salary):
    N = len(ids)
    copy_ids = copy(ids)
    copy_ids = sort(3, copy_ids)

    index_ids = []
    for i in range(N):
        for j in range(len(ids)):
            if(copy_ids[j] == ids[i]):
                index_ids.append(j)
                continue
    
    copy_salary = copy(salary)
    copy_salary = sort(3, copy_salary)
    
    for m in range(len(copy_salary)):
        for k in range(0, len(copy_salary)):
            if(index_ids[k] == m):
                salary[k] = copy_salary[m]
                break
    return salary