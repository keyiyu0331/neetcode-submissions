class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        res = []
        for s in strs:
            key = "".join(sorted(s))
            if key in group:
                group[key].append(s)
            else:
                group[key] = [s]
        
        for v in group.values():
            res.append(v)
        
        return res
        