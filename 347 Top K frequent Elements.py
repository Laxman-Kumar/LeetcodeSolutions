from collections import Counter
def topKFrequent(nums,k):
    #x = Counter(nums).most_common()[0:k]
    #print(x)
    return [z[0] for z in Counter(nums).most_common()[0:k]]
        
print(topKFrequent([1,1,1,2,2,3],2))
