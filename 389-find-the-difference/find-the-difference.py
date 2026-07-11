class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)
        
        for ch in t:
            if ch in s_list:
                s_list.remove(ch)
            else:
                return ch