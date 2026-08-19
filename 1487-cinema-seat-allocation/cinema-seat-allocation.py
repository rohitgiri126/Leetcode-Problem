from collections import defaultdict
from typing import List


class Solution:

  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    occupied = defaultdict(int)

    for row, seat in reservedSeats:
      if 2 <= seat <= 9:
        occupied[row] |= 1 << (seat - 1)

    left_mask = 0b000011110  
    right_mask = 0b111100000  
    middle_mask = 0b001111000  

    ans = (n - len(occupied)) * 2

    for mask in occupied.values():
      left = (mask & left_mask) == 0
      right = (mask & right_mask) == 0
      middle = (mask & middle_mask) == 0

      if left and right:
        ans += 2
      elif left or right or middle:
        ans += 1

    return ans