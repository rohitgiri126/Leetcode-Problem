class Solution:
    def minimumChanges(self, s: str, n: int) -> int:
        length = len(s)
        
        divisors = [[] for _ in range(length + 1)]
        for i in range(1, length + 1):
            for j in range(2 * i, length + 1, i):
                divisors[j].append(i)
                
        cost = [[float('inf')] * (length + 1) for _ in range(length + 1)]
        for i in range(length):
            for j in range(i + 1, length + 1):
                sub_len = j - i
                min_changes_for_d = float('inf')
                for d in divisors[sub_len]:
                    current_cost = 0
                    for offset in range(d):
                        left = i + offset
                        right = i + sub_len - 1 - (d - 1 - offset)
                        while left < right:
                            if s[left] != s[right]:
                                current_cost += 1
                            left += d
                            right -= d
                    if current_cost < min_changes_for_d:
                        min_changes_for_d = current_cost
                cost[i][j] = min_changes_for_d
                
        dp = [[float('inf')] * (n + 1) for _ in range(length + 1)]
        dp[0][0] = 0
        
        for i in range(1, length + 1):
            for k in range(1, min(i, n) + 1):
                for j in range((k - 1) * 2, i - 1):
                    if dp[j][k - 1] != float('inf') and cost[j][i] != float('inf'):
                        dp[i][k] = min(dp[i][k], dp[j][k - 1] + cost[j][i])
                        
        return dp[length][n]