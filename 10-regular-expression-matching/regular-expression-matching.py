class Solution:

  def isMatch(self, s: str, p: str) -> bool:
    memo = {}

    def dfs(i: int, j: int) -> bool:
      # If result is already computed, return it
      if (i, j) in memo:
        return memo[(i, j)]

      # Base Cases
      if j == len(p):
        return i == len(s)

      # Check if current characters match
      match = (i < len(s)) and (p[j] == s[i] or p[j] == ".")

      # If next character is '*'
      if (j + 1) < len(p) and p[j + 1] == "*":
        # Choice 1: Ignore '*' and preceding element (0 occurrences)
        # Choice 2: Use '*' if current characters match (1 or more occurrences)
        ans = dfs(i, j + 2) or (match and dfs(i + 1, j))
        memo[(i, j)] = ans
        return ans

      # Standard character match without '*'
      if match:
        ans = dfs(i + 1, j + 1)
        memo[(i, j)] = ans
        return ans

      memo[(i, j)] = False
      return False

    return dfs(0, 0)