class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")":"(", "]":"[", "}":"{"}
        stack = []
        for ch in s:
            if ch in pair:
                if stack and stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack
                
        