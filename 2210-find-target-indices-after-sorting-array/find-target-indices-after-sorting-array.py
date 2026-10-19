class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = 0
        count = 0

        for num in nums:
            if num < target:
                less += 1
            elif num == target:
                count += 1

        return list(range(less, less + count))