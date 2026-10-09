class Solution:

    def encode(self, strs: List[str]) -> str:
        res = str([len(s) for s in strs])
        for s in strs:
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        header_idx = s.index("]")
        header = s[1: header_idx]
        print(header)
        length = header.split(",")
        print(length)
        start = header_idx + 1
        res = []
        for i in length:
            print("this is i: " + i)
            i = int(i)
            res.append(s[start: start + i])
            start += i
        return res


        
