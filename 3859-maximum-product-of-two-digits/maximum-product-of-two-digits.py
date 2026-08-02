class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        a = []
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                a.append(int(s[i]) * int(s[j]))
        return max(a)