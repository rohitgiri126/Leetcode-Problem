import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(weight, idx) for idx, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        ans = []
        current_time = 0
        
        for task_idx, duration in enumerate(tasks):
            current_time = max(current_time, task_idx)
            
            if not free_servers:
                current_time = busy_servers[0][0]
            
            while busy_servers and busy_servers[0][0] <= current_time:
                finish_time, weight, server_idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, server_idx))
            
            weight, server_idx = heapq.heappop(free_servers)
            ans.append(server_idx)
            heapq.heappush(busy_servers, (current_time + duration, weight, server_idx))
            
        return ans