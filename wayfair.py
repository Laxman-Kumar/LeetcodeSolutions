def solution(N):
    if(N<0):
        x = str(N)[1:]
        temp=int('5'+x)
        for i in range(1,len(x)):
            y = x[:i]+'5'+x[i:]
            temp = min(int(y),temp)
        
        return int('-'+str(min(temp,int(x+'5'))))
    else:
        x = str(N)
        temp=int('5'+x)
        for i in range(1,len(x)):
            y = x[:i]+'5'+x[i:]
            temp = max(int(y),temp)
        return max(temp,int(x+'5'))

print(solution(670))
print(solution(8000))
print(solution(-4760))

