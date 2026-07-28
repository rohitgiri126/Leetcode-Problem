class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        points = {}
        for num in nums:
            points[num] = points.get(num, 0) + num

       
        unique_nums = sorted(points.keys())

        two_back = 0  
        one_back = 0 

        for i in range(len(unique_nums)):
            current_num = unique_nums[i]
            current_points = points[current_num]

            if i > 0 and current_num == unique_nums[i - 1] + 1:
                current_max = max(one_back, two_back + current_points)
            else:
                
                current_max = one_back + current_points

            two_back = one_back
            one_back = current_max

        return one_back