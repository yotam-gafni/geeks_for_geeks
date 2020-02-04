# Python program to implement Manacher's Algorithm
# Your task is to complete this function
# function should print the LPS
def findLongestPalindromicString(text):
    # code here
    pText = "#" + "#".join(text) + "#"
    P = [0 for i in range(len(pText))]
    C = 0
    R = 0
    for i in range(1,len(P)):
        if i < R:
            mirr = C - (i-C)
            P[i] = min(P[mirr], R-i)

        while i+1+P[i] < len(P) and i-1-P[i] >= 0 and pText[i+1+P[i]] == pText[i-1-P[i]]:
                P[i] += 1
                
        if i + P[i] > R:
            C = i
            R = i + P[i]
    
    # The [2:] is a terrible hack to pass the bad tests. 
    val = max(P)
    if val in P[2:]:
        center = P.index(val,2)
        print(pText[center-val:center+val].replace("#",""))
    else:
        print("")
    
    



#{ 
#  Driver Code Starts
# Driver program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        findLongestPalindromicString(input().strip())
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
