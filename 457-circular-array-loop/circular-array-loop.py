class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def get_next(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = get_next(i)

            while nums[i] * nums[fast] > 0 and nums[i] * nums[get_next(fast)] > 0:
                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True
                slow = get_next(slow)
                fast = get_next(get_next(fast))

            curr = i
            val = nums[i]
            while nums[curr] * val > 0:
                nxt = get_next(curr)
                nums[curr] = 0
                curr = nxt

        return False