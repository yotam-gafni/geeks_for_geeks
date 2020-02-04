#code
from heapq import heappush, heappop

t = int(input())

all_num = [1]
cand_list = []
cand_set = {}
has_been = {}
for i in range(10**4):
    if all_num[-1] * 2 not in cand_set and all_num[-1] * 2 not in has_been:
        cand_set[all_num[-1] * 2] = True
        heappush(cand_list, all_num[-1] * 2)
    if all_num[-1] * 3 not in cand_set and all_num[-1] * 3 not in has_been:
        cand_set[all_num[-1] * 3]= True
        heappush(cand_list, all_num[-1] * 3)
    if all_num[-1] * 5 not in cand_set and all_num[-1] * 5 not in has_been:
        cand_set[all_num[-1] * 5]= True
        heappush(cand_list, all_num[-1] * 5)

    min_cand = heappop(cand_list)
    has_been[min_cand] = True
    
    all_num.append(min_cand)


for _ in range(t):
    n = int(input())

 
    print(all_num[n-1])

        

