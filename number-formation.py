#code
import math


DEPTH = 101

res = [[[0 for i in range(DEPTH)] for j in range(DEPTH)] for k in range(DEPTH)]

ten_x = [0]
for j in range(1,DEPTH*3):
    ten_x.append((ten_x[-1] * 10 + 1) %  (10**9+ 7))

mod_inv = [0]
for i in range(1,DEPTH):
    mod_inv.append(pow(i,10**9 + 5, 10**9 + 7))
    
    
coeff = [[[1 for i in range(DEPTH)] for j in range(DEPTH)] for k in range(DEPTH)]

for x in range(DEPTH):
    for y in range(DEPTH):
        for z in range(DEPTH):
            if x > 0:
                coeff[x][y][z] = coeff[x-1][y][z] * (x+y+z)  *mod_inv[x] % (10**9 + 7)
            elif y > 0:
                coeff[x][y][z] = coeff[x][y-1][z]  * (x+y+z) * mod_inv[y] % (10**9 + 7)
            elif z > 0:
                coeff[x][y][z] = coeff[x][y][z-1] * (x+y+z)  * mod_inv[z] % (10**9 + 7)

for x in range(DEPTH):
    for y in range(DEPTH):
        for z in range(DEPTH):
            if x > 0:
                #coeff1 = int(math.factorial(x+y+z-1) / (math.factorial(x-1)*math.factorial(y)*math.factorial(z))) % (10**9+ 7)
                res[x][y][z] += (4 * coeff[x-1][y][z] * ten_x[x+y+z]) % (10**9+ 7)
            
            if y > 0:
                #coeff2 = int(math.factorial(x+y+z-1) / (math.factorial(x)*math.factorial(y-1)*math.factorial(z))) % (10**9+ 7)
                res[x][y][z] += (5 * coeff[x][y-1][z] * ten_x[x+y+z]) % (10**9+ 7)
            
            if z > 0:
                #coeff3 = int(math.factorial(x+y+z-1) / (math.factorial(x)*math.factorial(y)*math.factorial(z-1))) % (10**9+ 7)
                res[x][y][z] += (6 * coeff[x][y][z-1] * ten_x[x+y+z]) % (10**9+ 7)

                

t = int(input())

for _ in range(t):
    X, Y, Z = [int(i) for i in input().split(" ")]
    end_sum = 0
    for x in range(X+1):
        for y in range(Y+1):
            for z in range(Z+1):
                end_sum += (res[x][y][z]) % (10**9+ 7)


    print(end_sum % (10**9+ 7))


