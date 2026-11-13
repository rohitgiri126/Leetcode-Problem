from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        ans = 0
        cur_op = 0
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            while dq and nums[dq[-1]] <= nums[l]:
                idx = dq.pop()
                next_idx = dq[-1] if dq else r + 1
                cur_op += (next_idx - idx) * (nums[l] - nums[idx])
            
            dq.append(l)
            
            while cur_op > k:
                cur_op -= nums[dq[0]] - nums[r]
                if dq[0] == r:
                    dq.popleft()
                r -= 1
                
            ans += r - l + 1
            
        return ans