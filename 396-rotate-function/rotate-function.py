class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        current_val = sum(i * val for i, val in enumerate(nums))
        max_val = current_val

        for k in range(1, n):
            current_val += total_sum - n * nums[n - k]
            if current_val > max_val:
                max_val = current_val

        return max_val