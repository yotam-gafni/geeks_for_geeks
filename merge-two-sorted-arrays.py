#code

#from heapq import merge

class VirArr(object):
	def __init__(self, arr1,arr2):
		self.arr1 = arr1
		self.arr2 = arr2

	def __getitem__(self, t):
		if t < len(self.arr1):
			return self.arr1[t]
		else:
			return self.arr2[t - len(arr1)]

	def __setitem__(self, t, val):
		if t < len(arr1):
			self.arr1[t] = val
		else:
			self.arr2[t - len(arr1)] = val

	def print(self):
		print(" ".join([str(i) for i in self.arr1 + self.arr2]))


t = int(input())

for _ in range(t):
    m, n = [int(j) for j in str(input()).split(" ")]
    arr1 = [int(j) for j in filter(lambda x: x.isdigit(), input().split(" "))]
    arr2 = [int(j) for j in filter(lambda x: x.isdigit(), input().split(" "))]

    #print(*list(merge(arr1,arr2)))
    k = (m+n) // 2 + ((m+n) %2)
    virarr = VirArr(arr1,arr2)
    while k >= 1:
    	for i in range(m+n-k):
    	    if virarr[i] > virarr[i+k]:
    	    	virarr[i], virarr[i+k] = virarr[i+k], virarr[i]
    	if k == 1:
    	 	k = 0
    	else:
    	 	k = k // 2 + k%2
    
    virarr.print()
    
    
                
                
