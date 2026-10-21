class Solution:
    def minOperations(self, s: str) -> int:
        if list(s) == sorted(s):
            return 0
        
        n = len(s)
        if n <= 2:
            return -1

        min_char = min(s)
        max_char = max(s)

        if s[0] == min_char or s[-1] == max_char:
            return 1

        if min_char in s[:-1] or max_char in s[1:]:
            return 2

        return 3