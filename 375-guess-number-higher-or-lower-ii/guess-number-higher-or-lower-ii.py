class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                end = start + length - 1
                min_cost = float('inf')

                for x in range(start, end):
                    cost = x + max(dp[start][x - 1], dp[x + 1][end])
                    min_cost = min(min_cost, cost)

                dp[start][end] = min_cost

        return dp[1][n]