class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0
        
        for num in store:
            if num - 1 not in store:
                cur = num
                length = 1
                while cur + 1 in store:
                    cur += 1
                    length += 1
                longest = max(length, longest)
        return longest
                