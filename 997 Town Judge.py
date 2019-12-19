import operator

def findJudge(N,trust):
        t =[]
        trusted ={}
        for x in trust:
            t.append(x[0])
            if x[1] in trusted.keys():
                trusted[x[1]] = trusted[x[1]]+1
            else:trusted[x[1]]=1
                
        x = max(trusted.items(), key=operator.itemgetter(1))
        if x[1] == N-1 and x[0] not in t:return x[0]
        else:return -1
        #if len(set(trusted)-set(trust))!=0:
        #    return list(set(trusted)-set(trust))[0]
        #else: return -1

print(findJudge(2,[[1,2]]))
