class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        strs = [str(num) for num in nums]
        n = len(strs)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if strs[j] + strs[j + 1] < strs[j + 1] + strs[j]:
                    strs[j], strs[j + 1] = strs[j + 1], strs[j]
        
        if strs[0] == "0":
            return "0"
            
        return "".join(strs)