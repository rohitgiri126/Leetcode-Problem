class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        
        count9 = sum // 9
        rem = sum % 9
        
        if count9 == num:
            return "9" * num
        
        parts = ["9" * count9]
        if rem > 0:
            parts.append(str(rem))
            zeros = num - count9 - 1
        else:
            zeros = num - count9
            
        parts.append("0" * zeros)
        return "".join(parts)