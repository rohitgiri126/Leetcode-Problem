class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        point_map = {}
        for num in nums:
            point_map[num] = point_map.get(num, 0) + num
            
        sorted_keys = sorted(point_map.keys())
        
        take = 0
        skip = 0
        prev_key = -1
        
        for key in sorted_keys:
            current_points = point_map[key]
        
            if key == prev_key + 1:
                new_take = skip + current_points
                new_skip = max(take, skip)
            else:
                new_take = max(take, skip) + current_points
                new_skip = max(take, skip)
                
            take, skip = new_take, new_skip
            prev_key = key
            
        return max(take, skip)