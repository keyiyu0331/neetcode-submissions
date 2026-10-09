class Solution:

    def encode(self, strs: List[str]) -> str:
        length = [len(s) for s in strs]
        output = str(length)
        for s in strs:
            output += s
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        
        header = s.index("]")
        length = s[1:header]
        length = length.split(",")
        
        start = header + 1
        output = []
        for l in length:
            output.append(s[start : start+int(l)])
            start += int(l)
        return output