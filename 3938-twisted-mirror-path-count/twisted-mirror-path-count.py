class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 1_000_000_007

        nxt = [[[None, None] for _ in range(n)] for _ in range(m)]

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                for d in (0, 1):
                    if grid[r][c] == 0:
                        nxt[r][c][d] = (r, c)
                    else:
                        nr, nc, nd = (r + 1, c, 1) if d == 0 else (r, c + 1, 0)
                        if nr < m and nc < n:
                            nxt[r][c][d] = nxt[nr][nc][nd]
                        else:
                            nxt[r][c][d] = None

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                cur = dp[r][c]
                if not cur or grid[r][c] == 1:
                    continue

                if c + 1 < n:
                    dest = nxt[r][c + 1][0]
                    if dest:
                        dp[dest[0]][dest[1]] = (dp[dest[0]][dest[1]] + cur) % MOD

                if r + 1 < m:
                    dest = nxt[r + 1][c][1]
                    if dest:
                        dp[dest[0]][dest[1]] = (dp[dest[0]][dest[1]] + cur) % MOD

        return dp[m - 1][n - 1]