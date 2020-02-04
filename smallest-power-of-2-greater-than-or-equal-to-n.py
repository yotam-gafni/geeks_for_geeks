#code
import math

t = int(input())

for i in range(0,t):
    n = int(input())
    print(2**(int(math.log(n,2))+1))
