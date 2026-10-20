class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([value, timestamp])
        else:
            self.data[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.data:
            return res
        
        lst = self.data[key]
        l, r = 0, len(lst) - 1

        while l <= r:
            m = (l + r) // 2
            if lst[m][1] <= timestamp:
                res = lst[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
