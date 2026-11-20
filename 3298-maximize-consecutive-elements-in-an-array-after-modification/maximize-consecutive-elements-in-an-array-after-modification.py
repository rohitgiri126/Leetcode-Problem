class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        ans = 0
        for x in nums:
            inc = dp.get(x, 0) + 1
            cur = dp.get(x - 1, 0) + 1
            dp[x + 1] = max(dp.get(x + 1, 0), inc)
            dp[x] = max(dp.get(x, 0), cur)
            ans = max(ans, dp[x + 1], dp[x])
        return ans