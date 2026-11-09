import heapq
from bisect import bisect_left, insort

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []
        available = list(range(k))
        count = [0] * k
        
        for i, (arr, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr:
                _, server_id = heapq.heappop(busy)
                idx = bisect_left(available, server_id)
                if idx == len(available) or available[idx] != server_id:
                    insort(available, server_id, lo=idx)
            
            if not available:
                continue
                
            preferred = i % k
            idx = bisect_left(available, preferred)
            if idx == len(available):
                idx = 0
                
            server_id = available.pop(idx)
            heapq.heappush(busy, (arr + l, server_id))
            count[server_id] += 1
            
        max_handled = max(count)
        return [i for i, c in enumerate(count) if c == max_handled]