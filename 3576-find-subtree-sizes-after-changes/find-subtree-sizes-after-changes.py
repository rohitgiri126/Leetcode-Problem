from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = parent[:]
        last_seen = [-1] * 26

        def find_ancestors(u: int) -> None:
            ch_idx = ord(s[u]) - ord('a')
            prev = last_seen[ch_idx]
            if prev != -1:
                new_parent[u] = prev
            last_seen[ch_idx] = u
            for v in adj[u]:
                find_ancestors(v)
            last_seen[ch_idx] = prev

        find_ancestors(0)

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [0] * n

        def count_subtree(u: int) -> int:
            size = 1
            for v in new_adj[u]:
                size += count_subtree(v)
            ans[u] = size
            return size

        count_subtree(0)
        return ans