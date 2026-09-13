from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        points1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        points2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        delta_counts = Counter()
        for r1, c1 in points1:
            for r2, c2 in points2:
                delta = (r2 - r1, c2 - c1)
                delta_counts[delta] += 1
                
        return max(delta_counts.values()) if delta_counts else 0