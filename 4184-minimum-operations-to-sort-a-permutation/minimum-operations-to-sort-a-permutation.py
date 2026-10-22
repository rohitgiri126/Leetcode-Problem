class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        pos0 = nums.index(0)

        is_inc = True
        for i in range(n):
            if nums[(pos0 + i) % n] != i:
                is_inc = False
                break

        is_dec = True
        for i in range(n):
            if nums[(pos0 - i) % n] != i:
                is_dec = False
                break

        if not is_inc and not is_dec:
            return -1

        ans = float("inf")

        if is_inc:
            ans = min(ans, pos0)
            ans = min(ans, 1 + (n - pos0) % n + 1)

        if is_dec:
            ans = min(ans, 1 + (n - 1 - pos0) % n)
            ans = min(ans, (pos0 + 1) % n + 1)

        return ans