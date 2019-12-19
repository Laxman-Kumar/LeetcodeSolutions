def groupAnagrams(strs):
        from itertools import groupby
        y = ["".join(sorted(t)) for t in strs]
        print(y)
        res = [list(group) for key,group in groupby(sorted(strs,key=sorted),sorted)]
        return res

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
