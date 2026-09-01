from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_map = {}
        start_r = start_c = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = len(litter_map)

        target_mask = (1 << len(litter_map)) - 1
        if target_mask == 0:
            return 0

        best_energy = [[[-1] * (1 << len(litter_map)) for _ in range(n)] for _ in range(m)]
        best_energy[start_r][start_c][0] = energy

        queue = deque([(start_r, start_c, 0, energy, 0)])

        while queue:
            r, c, mask, cur_energy, steps = queue.popleft()

            if mask == target_mask:
                return steps

            if cur_energy == 0:
                continue

            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = cur_energy - 1
                    nmask = mask
                    cell = classroom[nr][nc]

                    if cell == 'L':
                        nmask |= (1 << litter_map[(nr, nc)])
                    elif cell == 'R':
                        ne = energy

                    if ne > best_energy[nr][nc][nmask]:
                        best_energy[nr][nc][nmask] = ne
                        queue.append((nr, nc, nmask, ne, steps + 1))

        return -1