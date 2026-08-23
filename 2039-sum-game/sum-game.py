class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        diff = 0
        q_diff = 0
        
        for i in range(mid):
            if num[i] == '?':
                q_diff += 1
            else:
                diff += int(num[i])
                
        for i in range(mid, n):
            if num[i] == '?':
                q_diff -= 1
            else:
                diff -= int(num[i])
                
        return diff * 2 != -q_diff * 9