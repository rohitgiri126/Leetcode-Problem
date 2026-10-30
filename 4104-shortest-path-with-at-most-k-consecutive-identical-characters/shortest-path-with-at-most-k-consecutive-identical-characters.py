from collections import defaultdict
import heapq


class Solution:

  def shortestPath(
      self, n: int, edges: list[list[int]], labels: str, k: int
  ) -> int:
    adj = defaultdict(list)
    for u, v, w in edges:
      adj[u].append((v, w))

    dist = {}
    dist[(0, 1)] = 0
    pq = [(0, 0, 1)]

    while pq:
      d, u, count = heapq.heappop(pq)

      if u == n - 1:
        return d

      if d > dist.get((u, count), float("inf")):
        continue

      for v, w in adj[u]:
        next_count = count + 1 if labels[u] == labels[v] else 1
        if next_count > k:
          continue

        next_dist = d + w
        if next_dist < dist.get((v, next_count), float("inf")):
          dist[(v, next_count)] = next_dist
          heapq.heappush(pq, (next_dist, v, next_count))

    return -1