class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.sum_val = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 1_000_000_007

    def _apply(self, idx: int, l: int, r: int, val: int):
        val %= self.MOD
        length = r - l + 1
        
        term1 = self.sum_sq[idx]
        term2 = (2 * val * self.sum_val[idx]) % self.MOD
        term3 = (length * ((val * val) % self.MOD)) % self.MOD
        self.sum_sq[idx] = (term1 + term2 + term3) % self.MOD
        
        self.sum_val[idx] = (self.sum_val[idx] + length * val) % self.MOD
        self.lazy[idx] = (self.lazy[idx] + val) % self.MOD

    def _push(self, idx: int, l: int, r: int):
        if self.lazy[idx] != 0:
            mid = (l + r) // 2
            self._apply(2 * idx, l, mid, self.lazy[idx])
            self._apply(2 * idx + 1, mid + 1, r, self.lazy[idx])
            self.lazy[idx] = 0

    def update(self, idx: int, l: int, r: int, ql: int, qr: int, val: int):
        if ql <= l and r <= qr:
            self._apply(idx, l, r, val)
            return

        self._push(idx, l, r)
        mid = (l + r) // 2

        if ql <= mid:
            self.update(2 * idx, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * idx + 1, mid + 1, r, ql, qr, val)

        self.sum_val[idx] = (self.sum_val[2 * idx] + self.sum_val[2 * idx + 1]) % self.MOD
        self.sum_sq[idx] = (self.sum_sq[2 * idx] + self.sum_sq[2 * idx + 1]) % self.MOD


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 1_000_000_007
        
        st = SegmentTree(n)
        last_occurrence = {}
        total_ans = 0

        for i, val in enumerate(nums):
            prev = last_occurrence.get(val, -1)
            st.update(1, 0, n - 1, prev + 1, i, 1)
            last_occurrence[val] = i
            total_ans = (total_ans + st.sum_sq[1]) % MOD

        return total_ans