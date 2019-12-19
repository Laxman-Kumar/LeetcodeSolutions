def solution(s,t):
    count ={}
    for i in range(0,len(s)):
        count[s[i]]=count[s[i]]+1
        count[t[i]]=count[t[i]]-1

    for x in count:
        if(count[x]!=0):return False

    return True

print(solution('anagram','nagaram'))
