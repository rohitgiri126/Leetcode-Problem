import sys

sys.setrecursionlimit(200000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        up = [[0] * 17 for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        chars = list(s)

        stack = [(0, -1, 0)]
        adj_idx = [0] * n

        timer = 1
        tin[0] = 1
        up[0][0] = 0

        while stack:
            u, p, d = stack[-1]
            if adj_idx[u] == 0:
                depth[u] = d
                up[u][0] = p if p != -1 else 0
                for i in range(1, 17):
                    up[u][i] = up[up[u][i - 1]][i - 1]

            if adj_idx[u] < len(adj[u]):
                v = adj[u][adj_idx[u]]
                adj_idx[u] += 1
                if v != p:
                    timer += 1
                    tin[v] = timer
                    stack.append((v, u, d + 1))
            else:
                tout[u] = timer
                stack.pop()

        bit = [0] * (n + 2)

        def bit_update(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)

        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        for i in range(n):
            mask = 1 << (ord(chars[i]) - 97)
            bit_update(tin[i], mask)
            bit_update(tout[i] + 1, mask)

        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(17):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(16, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                old_c = chars[u]
                if old_c != new_c:
                    chars[u] = new_c
                    xor_diff = (1 << (ord(old_c) - 97)) ^ (1 << (ord(new_c) - 97))
                    bit_update(tin[u], xor_diff)
                    bit_update(tout[u] + 1, xor_diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                mask_lca_char = 1 << (ord(chars[lca]) - 97)
                
                path_mask = mask_u ^ mask_v ^ mask_lca_char
                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans