class TimeMap:

    def __init__(self):
        self.data = {} # {"alice" : [["happy", 1], ["sad", 2]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([value, timestamp])
        else:
            self.data[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        
        if key not in self.data:
            return res
        
        target = self.data[key]
        l, r = 0, len(target) - 1
        while l <= r:
            m = (l + r) // 2
            if target[m][1] <= timestamp:
                res = target[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

