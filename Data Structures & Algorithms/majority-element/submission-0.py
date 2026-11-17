from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, maxCount = 0, 0
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
            res = n if counts[n] > maxCount else res
            maxCount = max(maxCount, counts[n])
        return res
            

        