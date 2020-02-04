#code
import copy

def printPal(arr):
    even = len(arr) % 2 == 0
    mid = int(len(arr) / 2) - 1 * even
    ind = len(arr) - 1
    while ind > mid:
        if arr[ind] > arr[2 * mid + 1 * even - ind]:
            arr[ind] = arr[2 * mid + 1 * even - ind]
            stop_point = ind - 1
            while arr[stop_point] == 9:
                arr[stop_point] = (arr[stop_point] + 1) % 10
                stop_point -= 1
            arr[stop_point] = (arr[stop_point] + 1) % 10
        else:
            arr[ind] = arr[2 * mid + 1 * even - ind]
        ind -= 1

    """takin = True

    for j in range(1, mid + 1):
        if arr[mid + j + 1 * even] > arr[mid - j]:
            takin = False
    if not takin:
        stop_point = mid
        while arr[stop_point] == 9:
            arr[stop_point] = (arr[stop_point] + 1) % 10
            stop_point -= 1
        
        arr[stop_point] = (arr[stop_point] + 1) % 10"""
    for j in range(mid + 1):
        arr[mid + 1 * even + j] = arr[mid - j]
    
    return 
    #print(" ".join([str(i) for i in arr]))
    #return 


        
        
t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(elem) for elem in filter(lambda x: x.isdigit(), str(input()).split(' '))]
    #print(" ".join([str(i) for i in arr[500:]]))
    orig = copy.copy(arr)
    printPal(arr)
    if orig == arr:
        arr[-1] = (arr[-1] + 1) % 10
        stop_point = len(arr) - 2
        while arr[stop_point] == 9 and stop_point >= 0:
            arr[stop_point] = (arr[stop_point] + 1) % 10
            stop_point -= 1
        if stop_point < 0 and arr[0] == 0:
            arr = [1] + [0] * (len(arr) - 1) + [1]
        elif stop_point >=0:
            arr[stop_point] = (arr[stop_point] + 1) % 10
        
        printPal(arr)
    print(" ".join([str(i) for i in arr]))
        


