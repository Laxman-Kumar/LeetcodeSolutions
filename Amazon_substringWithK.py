from itertools import combinations
def substringExactlyK(s,k):
    if(len(set(s))<k):return 0
    else:
        all_combinations = list(s[i:j+1] for i in range (len(s)) for j in range(i,len(s)))
        temp =[]
        for i in all_combinations:
            if(len(set(i))==k and i in s):temp.append(i)
        return len(temp)

print(substringExactlyK('aabab',3))

