def solution(A,K):
    res = []
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if len(set(A[i:j+1]))==2:
                res.append(A[i:j+1])
    return len(res)

print(solution([1,2,1,2,3],2))
