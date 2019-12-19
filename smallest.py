
    
def findSmallestt(A):
   
    if 1 not in A:
        return 1
    else:
        for i in range(len(A)):
            if i+1 not in A:
                return i+1
    return max(A)+1


x = [1,3,6,4,1,2]




y = [1,2,3]
z = [-1,-3]




print(findSmallestt(z))
#print(findSmallest(y))
#print(findSmallest(z))
