class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        sorted_logs = sorted(logs, key=lambda l: l[1])
        
        res = [0] * len(queries)
        active_servers = {}
        log_idx = 0
        m = len(sorted_logs)
        
        left = 0
        right = 0
        
        for q_idx, q_time in indexed_queries:
            start_time = q_time - x
            
            while right < m and sorted_logs[right][1] <= q_time:
                server_id = sorted_logs[right][0]
                active_servers[server_id] = active_servers.get(server_id, 0) + 1
                right += 1
                
            while left < m and sorted_logs[left][1] < start_time:
                server_id = sorted_logs[left][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                left += 1
                
            res[q_idx] = n - len(active_servers)
            
        return res