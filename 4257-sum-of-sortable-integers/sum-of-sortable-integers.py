class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        ans = 0
        for k in divisors:
            possible = True
            for i in range(0, n, k):
                if k == 1:
                    if nums[i] != s[i]:
                        possible = False
                        break
                    continue
                
                drop_idx = -1
                descent_count = 0
                for j in range(k - 1):
                    if nums[i + j] > nums[i + j + 1]:
                        descent_count += 1
                        drop_idx = j
                
                if descent_count > 1:
                    possible = False
                    break
                
                if descent_count == 1:
                    if nums[i + k - 1] > nums[i]:
                        possible = False
                        break
                    start = drop_idx + 1
                else:
                    start = 0
                
                match = True
                for j in range(k):
                    if nums[i + (start + j) % k] != s[i + j]:
                        match = False
                        break
                
                if not match:
                    possible = False
                    break
            
            if possible:
                ans += k
                
        return ans