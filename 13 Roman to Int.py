def romanToInteger(s):
    val = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    choice = True
    i=0
    ans = 0
    while(choice):
        if(i<len(s)-1):
            if(s[i]=="I" and s[i+1] in ["V","X"]):
                ans = ans+(val[s[i+1]]-1)
                i = i+2
            elif(s[i]=="X" and s[i+1] in ["L","C"]):
                ans = ans+(val[s[i+1]]-10)
                i=i+2
            elif(s[i]=="C" and s[i+1] in ["D","M"]):
                ans = ans+(val[s[i+1]]-100)
                i=i+2
            else:
                ans = ans+val[s[i]]
                i = i+1
        else:
            ans = ans+val[s[i]]
            i = i+1
        if(i>=len(s)):choice=False
        
    return ans
print(romanToInteger("IV"))
print(romanToInteger("IX"))
print(romanToInteger("LVIII"))
