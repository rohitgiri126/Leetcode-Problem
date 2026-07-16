import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        
        current_max = 0
        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(math.gcd(num, current_max))
        
        prefixGcd.sort()
        
        left = 0
        right = n - 1
        total_gcd_sum = 0
        
        while left < right:
            total_gcd_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_gcd_sum