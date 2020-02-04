#code

t = int(input())

for i in range(t):
    n = int(input())
    dn = int(input())
    outer = int(n/dn)
    inner = n - dn*outer
    inner_list = []
    dec = []
    while inner not in inner_list and inner != 0:
        inner_list.append(inner)
        dec.append(str(int(inner*10 / dn)))
        inner = inner*10 - int(inner*10 / dn) * dn
    
    if inner==0:
        pr_dec = ''.join(dec)
        if pr_dec == "":
            print("{}".format(outer))
        else:
            print("{}.{}".format(outer,pr_dec))
    else:
        splitter = inner_list.index(inner)
        pre = dec[:splitter]
        post = dec[splitter:]
        pre_dec = ''.join(pre)
        post_dec = ''.join(post)
        print("{}.{}({})".format(outer, pre_dec, post_dec))
        
    
