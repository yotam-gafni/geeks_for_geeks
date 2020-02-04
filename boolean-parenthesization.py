#code

def printBE(n, be):
    be_count = be.count("T") + be.count("F")
    operators = list(be.replace("F","").replace("T","").strip())
    dyn_dict = {}
    
    t_values = list(filter(lambda x: x=="F" or x=="T", be))
    
    for j in range(0, be_count):
        if t_values[j] == "T":
            dyn_dict[tuple([j,j,"T"])] = 1
            dyn_dict[tuple([j,j,"F"])] = 0
        else:
            dyn_dict[tuple([j,j,"F"])] = 1
            dyn_dict[tuple([j,j,"T"])] = 0        
    
    for batch_size in range(2,be_count+1):
        for s in range(0, be_count - batch_size + 1):
            dyn_dict[tuple([s, s+batch_size-1, "T"])] = 0
            dyn_dict[tuple([s, s+batch_size-1, "F"])] = 0
            for op_ind in range(s,s+batch_size - 1):
                if operators[op_ind] == "&":
                    dyn_dict[tuple([s, s+batch_size-1, "T"])] += dyn_dict[tuple([s, op_ind, "T"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "T"])]
                    dyn_dict[tuple([s, s+batch_size-1, "F"])] += dyn_dict[tuple([s, op_ind, "F"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "F"])]
                    dyn_dict[tuple([s, s+batch_size-1, "F"])] += dyn_dict[tuple([s, op_ind, "T"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "F"])]
                    dyn_dict[tuple([s, s+batch_size-1, "F"])] += dyn_dict[tuple([s, op_ind, "F"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "T"])]
                if operators[op_ind] == "|":
                    dyn_dict[tuple([s, s+batch_size-1, "T"])] += dyn_dict[tuple([s, op_ind, "T"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "T"])]
                    dyn_dict[tuple([s, s+batch_size-1, "F"])] += dyn_dict[tuple([s, op_ind, "F"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "F"])]
                    dyn_dict[tuple([s, s+batch_size-1, "T"])] += dyn_dict[tuple([s, op_ind, "T"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "F"])]
                    dyn_dict[tuple([s, s+batch_size-1, "T"])] += dyn_dict[tuple([s, op_ind, "F"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "T"])]
                if operators[op_ind] == "^":
                    dyn_dict[tuple([s, s+batch_size-1, "F"])] += dyn_dict[tuple([s, op_ind, "T"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "T"])]
                    dyn_dict[tuple([s, s+batch_size-1, "F"])] += dyn_dict[tuple([s, op_ind, "F"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "F"])]
                    dyn_dict[tuple([s, s+batch_size-1, "T"])] += dyn_dict[tuple([s, op_ind, "T"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "F"])]
                    dyn_dict[tuple([s, s+batch_size-1, "T"])] += dyn_dict[tuple([s, op_ind, "F"])] * dyn_dict[tuple([op_ind + 1, s+batch_size-1, "T"])]
    print(dyn_dict[tuple([0,be_count-1, "T"])] % 1003)
                    
                    
                    
      


t = int(input())

for i in range(t):
    n = int(input())
    be = str(input())
    
    printBE(n, be)
                  
                    
                    
                    
