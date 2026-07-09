class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        two_steps_back = 1 
        one_step_back = 2  
        
        for i in range(3, n + 1):
            current_ways = one_step_back + two_steps_back
            two_steps_back = one_step_back
            one_step_back = current_ways
            
        return one_step_back