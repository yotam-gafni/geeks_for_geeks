#code

t = int(input())

for _ in range(t):
    n, k = [int(i) for i in filter(lambda x: x.isdigit(), input().split(" "))]
    arr = [int(i) for i in filter(lambda x: x.isdigit(), input().split(" "))]
    total = 0
    temp = arr[-1]
    j = 0
    epsilon = 1/10**3

    for i in range(len(arr)):
        temp = temp / arr[i-1]

        while j < len(arr) and temp * arr[j] + epsilon < k:
            temp = temp * arr[j]
            j += 1
        total += (j-i)

    
    print(total)
        
            
     
