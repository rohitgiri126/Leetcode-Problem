class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        dp = {}
        
        def helper(i, M):
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix_sum[i]
            if (i, M) in dp:
                return dp[(i, M)]
            
            res = 0
            for X in range(1, 2 * M + 1):
                res = max(res, suffix_sum[i] - helper(i + X, max(M, X)))
            
            dp[(i, M)] = res
            return res
            
        return helper(0, 1)