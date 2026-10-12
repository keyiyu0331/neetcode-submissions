class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = None
        while l <= r:
            if nums[r] >= nums[l]:
                return nums[l]
            m = (l + r) // 2
            if nums[m] <= nums[r]:
                res = nums[m]
                r = m
            else:
                l = m + 1
        return res
                
                