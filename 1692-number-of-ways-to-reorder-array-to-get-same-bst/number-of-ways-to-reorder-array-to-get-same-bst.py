import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def ways(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            comb = math.comb(len(left) + len(right), len(left)) % MOD
            return (comb * ways(left) * ways(right)) % MOD

        return (ways(nums) - 1) % MOD