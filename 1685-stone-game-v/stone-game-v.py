from functools import lru_cache
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == j:
                return 0
            
            res = 0
            total = pref[j + 1] - pref[i]
            
            for k in range(i, j):
                left_sum = pref[k + 1] - pref[i]
                right_sum = total - left_sum
                
                if left_sum < right_sum:
                    res = max(res, left_sum + dp(i, k))
                elif left_sum > right_sum:
                    res = max(res, right_sum + dp(k + 1, j))
                else:
                    res = max(res, left_sum + max(dp(i, k), dp(k + 1, j)))
                    
            return res

        return dp(0, n - 1)