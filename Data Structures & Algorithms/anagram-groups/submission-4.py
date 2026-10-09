class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        ans_map = {}
        for s in strs:
            key = "".join(sorted(s))
            isGrouped = False
            if key in ans_map:
                ans_map[key].append(s)
                isGrouped = True
            if not isGrouped:
                ans_map[key] = [s]
        
        for v in ans_map.values():
            ans.append(v)

        return ans

        