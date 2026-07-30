class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        target = sorted(str(n))
        
        for i in range(30):
            power_of_two = 1 << i  
            if sorted(str(power_of_two)) == target:
                return True
                
        return False