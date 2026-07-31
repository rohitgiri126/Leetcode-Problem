class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def check(n1, n2, remaining):
            if not remaining:
                return True
            
            nxt = str(n1 + n2)
            if not remaining.startswith(nxt):
                return False
            
            return check(n2, n1 + n2, remaining[len(nxt):])

       
        for i in range(1, n):
            for j in range(i + 1, n):
                s1, s2 = num[:i], num[i:j]

                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue

                if check(int(s1), int(s2), num[j:]):
                    return True

        return False