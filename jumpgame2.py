def solution(data):
    i=0
    step=0
    while(i<len(data)-1):
        if(data[i+1]>1 and i+data[i+1]<len(data)-1 and data[i+1]>data[i]):
            i=i+1
            step=step+1
        else:
            i=i+data[i]
            step=step+1
        print(i)
        print(data[i])
            
    return step
    

print(solution([4,1,1,3,1,1,1]))
