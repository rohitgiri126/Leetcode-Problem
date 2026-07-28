class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(index: int, remaining: int) -> int:
            if remaining == 0:
                return 1
            
            if remaining < 0 or index == len(coins):
                return 0
            
            state = (index, remaining)
            if state in memo:
                return memo[state]

            take = dp(index, remaining - coins[index])
            skip = dp(index + 1, remaining)

            memo[state] = take + skip
            return memo[state]

        return dp(0, amount)