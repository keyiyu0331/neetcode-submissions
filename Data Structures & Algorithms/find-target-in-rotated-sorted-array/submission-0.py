class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[r] >= nums[l]:
                i, j = l, r

                while i <= j:
                    m = (i + j) // 2
                    if nums[m] > target:
                        j = m - 1
                    elif nums[m] < target:
                        i = m + 1
                    else:
                        return m
                return -1
            
            if target > nums[r] and l <= r:
                r -= 1
            elif target < nums[l] and l <= r:
                l += 1
        return -1
