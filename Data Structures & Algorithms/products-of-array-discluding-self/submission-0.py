class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_p = [1]
        for n in nums[::-1]:
            cur = n * suffix_p[-1]
            suffix_p.append(cur)

        suffix_p.pop()
        suffix_p.reverse()

        preffix_p = 1

        for idx in range(len(nums)):
            suffix_p[idx] *= preffix_p
            preffix_p *= nums[idx]

        return suffix_p