class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        
        for val in nums:
            nxt = [0] * k
            r = val % k
            nxt[r] += 1
            for j in range(k):
                if dp[j]:
                    nxt[(j * r) % k] += dp[j]
            dp = nxt
            for j in range(k):
                ans[j] += dp[j]
                
        return ans