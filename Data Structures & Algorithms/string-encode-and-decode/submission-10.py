class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_lengths = [len(s) for s in strs]
        #return [5, 5]HelloWorld
        print(str(strs_lengths) + "".join(strs))
        return str(strs_lengths) + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        
        header_idx = s.index(']')
        
        header = s[1:header_idx].split(", ")
        header = [int(n) for n in header]

        data = s[header_idx + 1:]

        res = []
        start = 0
        for n in header:
            
            res.append(data[start : start+n])
            start += n            

        return res