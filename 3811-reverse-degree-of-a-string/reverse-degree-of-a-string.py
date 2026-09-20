class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s, 1):
            rev_alphabet_pos = 26 - (ord(ch) - ord("a"))
            total += rev_alphabet_pos * i
        return total