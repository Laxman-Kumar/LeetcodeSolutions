def combinationSum(candidates,target):
    x = [t for t in candidates if target%t==0 ]
    print(x)



combinationSum([2,3,4,5],8)
