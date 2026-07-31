from collections import Counter


class Solution:

  def minimumPushes(self, word: str) -> int:
    counts = Counter(word)
    freqs = sorted(counts.values(), reverse=True)

    total_pushes = 0
    for i, freq in enumerate(freqs):
      pushes_required = (i // 8) + 1
      total_pushes += freq * pushes_required

    return total_pushes