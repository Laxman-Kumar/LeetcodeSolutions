class Solution:
    def intToRoman(self, num: int) -> str:
        val = {"1":"I","5":"V","10":"X","50":"L","100":"C","500":"D","1000":"M","4":"IV","9":"IX","40":"XL","90":"XC","400":"CD","900":"CM"}
        choice = True
        i=0
        ans = ""
        while(choice):
            if str(num) in val.keys():
                ans = ans+val[str(num)]
                num = 0
            else:
                if num<4:
                    ans = ans+"I"
                    num = num-1
                elif num>5 and num<9:
                    ans = ans+"V"
                    num = num-5
                elif num>10 and num<50:
                    ans = ans+ ("X"*(num//10))
                    num = num%10
                elif num>50 and num<100:
                    ans = ans+ ("L"*(num//50))
                    num = num%50
                elif num>100 and num<500:
                    ans = ans+ ("C"*(num//100))
                    num = num%100
                elif num>500 and num<1000:
                    ans = ans+ ("D"*(num//500))
                    num = num%500
                else:
                    ans = ans+ ("M"*(num//1000))
                    num = num%1000
            if num==0:
                choice=False
        if "CCCC" in ans:
            if ans[ans.find("CCCC")-1]=="D":
                ans = ans[:ans.find("CCCC")-1]+"CM"+ans[ans.find("CCCC")+4:]
            else:
                ans = ans[:ans.find("CCCC")]+"CD"+ans[ans.find("CCCC")+4:]
        if "XXXX" in ans:
            if ans[ans.find("XXXX")-1]=="L":
                ans = ans[:ans.find("XXXX")-1]+"XC"+ans[ans.find("XXXX")+4:]
            else:
                ans = ans[:ans.find("XXXX")]+"XL"+ans[ans.find("XXXX")+4:]
        return ans
