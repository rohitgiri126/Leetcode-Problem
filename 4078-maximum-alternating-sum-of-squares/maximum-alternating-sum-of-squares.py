class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = sorted(x * x for x in nums)
        n = len(sq)
        neg_count = n // 2
        return sum(sq[neg_count:]) - sum(sq[:neg_count])