#code

def max_cap(arr, cap):
    dyn_table = [0] * (cap + 1)
    for elem in arr:
        for i in range(len(dyn_table) - elem - 1, 0, -1):
            dyn_table[i+elem] = dyn_table[i] or dyn_table[i+elem]
        if elem <= cap:
            dyn_table[elem] = 1
    
    for i in range(len(dyn_table) -1, -1,-1):
        if dyn_table[i] == 1:
            return i
            
t = int(input())

for i in range(0,t):
    n = int(input())
    arr_str = str(input())
    arr = [int(elem) for elem in filter(lambda x: x.isdigit(), arr_str.split(' '))]
    sum_arr = sum(arr)
    res = max_cap(arr, int(sum_arr/2))
    print(int(sum_arr - 2*res))
