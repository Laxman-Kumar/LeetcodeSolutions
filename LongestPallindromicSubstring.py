"""
def longestPalindrome(s: str) -> str:
        ans = ""
        for i in range(0,len(s)):
            print("I value : ",str(i))
            for j in range(i,len(s)+1):
                print("J value : ",str(j))
                temp = s[i:j]
                if temp == temp[::-1]:
                    if len(temp)>len(ans):
                        ans = temp
                    
        return ans

print(longestPalindrome("a"))
"""
import math
def expandAroundCenter(s,left,right):
    while (left>0 and right < len(s) and s[left]==s[right]):
        left-=1
        right+=1
    return right - left - 1
        
def longestPalindrome(s: str) -> str:
    start =0
    end = 0
    for i in range(0,len(s)):
        len1 = expandAroundCenter(s,i,i)
        len2 = expandAroundCenter(s,i,i+1)
        lengt = max(len1,len2)
        if(lengt> end - start):
            start = i- (lengt -1)/2
            end = i+lengt/2
    print(end)            
    return s[start:end+1]

print(longestPalindrome("cbbd"))
