class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp0, dp1, dp2 = 0, float("inf"), float("inf")

        for j in range(1, n + 1):
            c = costs[j - 1]
            curr = min(dp0 + c + 1, dp1 + c + 4, dp2 + c + 9)
            dp0, dp1, dp2 = curr, dp0, dp1

        return dp0