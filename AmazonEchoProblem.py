from collections import Counter
import heapq
def amazonEcho(nC,tNC,comp,nR,rev):
    ans =[]
    for i in range(0,nR):
        ans.extend([x for x in comp if x in rev[i]])
        
    ans = Counter(ans)
    return heapq.nlargest(tNC, ans.keys(), key=ans.get)

comp = ["newshop","shopnow","afshion","fashionbeats","mymarket","tcelullar"]
reviews = ["newshop is a providing good services in the city, everyone; everyone should use newshop","best services by newshop","fashionbeats has great services in the city","I am proud to have fashionbeats","mymarket has awesome services","Thanks Newshop for the quick delivery"]

print(amazonEcho(6,2,comp,6,reviews))
