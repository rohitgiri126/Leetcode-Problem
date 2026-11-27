from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        max_f = max(f for f, _ in items)

        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        div_count = [0] * (max_f + 1)
        for d in range(1, max_f + 1):
            for mult in range(d, max_f + 1, d):
                div_count[d] += freq[mult]

        free_gain = [0] * n
        for i, (f, _) in enumerate(items):
            free_gain[i] = max(0, div_count[f] - 1)

        dp = [0] * (budget + 1)

        for i, (_, price) in enumerate(items):
            if price > budget:
                continue
            gain_first = 1 + free_gain[i]
            for b in range(budget, price - 1, -1):
                if dp[b - price] + gain_first > dp[b]:
                    dp[b] = dp[b - price] + gain_first

        for _, price in items:
            if price > budget:
                continue
            for b in range(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

        return max(dp)