class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        m = {")" : "(", "]" : "[", "}" : "{"}
        for ch in s:
            if ch in "([{":
                res.append(ch)
            else:
                if res and m[ch] == res[-1]:
                    res.pop()
                else:
                    return False

        return not res

        