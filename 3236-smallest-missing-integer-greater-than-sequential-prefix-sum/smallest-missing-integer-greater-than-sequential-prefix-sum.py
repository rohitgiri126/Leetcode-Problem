class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1
            
        num_set = set(nums)
        while s in num_set:
            s += 1
            
        return s