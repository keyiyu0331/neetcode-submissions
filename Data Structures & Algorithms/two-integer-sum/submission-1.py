class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_till_target = {}
    
        for idx in range(len(nums)):
            diff = target - nums[idx]
            n_till_target[diff] = idx
        
        for i, n in enumerate(nums):
            
            if n in n_till_target and n_till_target[n] != i:
                return [i, n_till_target[n]]