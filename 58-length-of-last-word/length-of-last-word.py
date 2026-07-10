class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() without arguments splits by any whitespace group
        words = s.split()
        return len(words[-1]) if words else 0