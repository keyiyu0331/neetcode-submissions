class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        data = set(nums)

        for n in nums:
            if n - 1 in data:
                continue
            count = 0
            while n in data:
                count += 1
                n += 1
            longest = max(longest, count)
        return longest