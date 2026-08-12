class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        length = max(len(v1), len(v2))
        v1.extend([0] * (length - len(v1)))
        v2.extend([0] * (length - len(v2)))
        
        for num1, num2 in zip(v1, v2):
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
                
        return 0