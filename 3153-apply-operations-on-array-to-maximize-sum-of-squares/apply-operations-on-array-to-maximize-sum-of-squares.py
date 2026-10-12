class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 1_000_000_007
        count = [0] * 31

        for x in nums:
            for bit in range(31):
                if (x >> bit) & 1:
                    count[bit] += 1

        ans = 0
        for _ in range(k):
            val = 0
            for bit in range(31):
                if count[bit] > 0:
                    val |= (1 << bit)
                    count[bit] -= 1
            ans = (ans + val * val) % MOD

        return ans