def allLengthNSubstring(data,k):
    temp=[]
    for i in range(0,(len(data)-k)):
        if(len(set(list(data[i:k+i])))==len(data[i:k+i])):
            temp.append(data[i:k+i])
    return temp



s = "awaglknagawunagwkwagl"
k = 4
print(allLengthNSubstring(s,k))
