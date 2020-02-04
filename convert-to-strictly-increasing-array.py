#code

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in filter(lambda x: x.isdigit(), input().split(" "))]
    dyn = [[] for i in arr]
    dyn[0].append([0,arr[0]])
    dyn[0].append([1,-len(arr)])
    for i in range(1,len(arr)):
        new_dyn = []
        if arr[i] > dyn[i-1][0][1]:
            new_dyn.append([dyn[i-1][0][0], arr[i]])
        for dyn_elem in dyn[i-1]:
            if arr[i] > dyn_elem[1]:
                new_dyn.append([dyn_elem[0], arr[i]])
                new_dyn.append([dyn_elem[0] + 1, dyn_elem[1]+1])
            else:
                new_dyn.append([dyn_elem[0] + 1, dyn_elem[1] + 1])
            unique_dict = {}
        for elem in new_dyn:
            if elem[0] not in unique_dict:
                unique_dict[elem[0]] = elem[1]
            else:
                unique_dict[elem[0]] = min(unique_dict[elem[0]], elem[1])
        dyn[i] = list(unique_dict.items())
    
    print(min([elem[0] for elem in dyn[-1]]))
