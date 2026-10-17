class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (get_digit_sum(x), x))
        target_pos = {val: i for i, val in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target_pos[nums[i]] == i:
                continue

            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = target_pos[nums[curr]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps