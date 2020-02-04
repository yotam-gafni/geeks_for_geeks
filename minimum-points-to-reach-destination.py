#code

t = int(input())

for _ in range(t):
    m,n = [int(i) for i in filter(lambda x: x.isdigit(), input().split(" "))]
    arr = [int(i) for i in filter(lambda x: x.lstrip('-').isdigit(), input().split(" "))]
    mat = [[0 for i in range(n)] for j in range(m)]
    dyn = [[[] for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            mat[i][j] = arr[i*n + j]
                
    for i in range(m):
        for j in range(n):
            working_list = []
            if i > 0:
                working_list += [[elem[0] + mat[i-1][j], elem[1]] for elem in dyn[i-1][j]]
            if j > 0:
                working_list += [[elem[0] + mat[i][j-1], elem[1]] for elem in dyn[i][j-1]]
            if i==0 and j==0:
                working_list = [[1,1]]

            for wl in working_list:
                if wl[0] < 1:
                    wl[1] += (1 - wl[0])
                    wl[0] = 1

            unique_val = {}
            for wl in working_list:
                if wl[0] not in unique_val:
                    unique_val[wl[0]] = wl[1]
                else:
                    unique_val[wl[0]] = min(unique_val[wl[0]], wl[1])
            dyn[i][j] = list(unique_val.items())

    final_list = [[elem[0] + mat[m-1][n-1],elem[1]] for elem in dyn[m-1][n-1]]
    for fl in final_list:
        if fl[0] < 1:
            fl[1] += (1 - fl[0])
            fl[0] = 1

    ans = min([elem[1] for elem in final_list])
    print(ans)
