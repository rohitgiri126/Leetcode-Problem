class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Last index se start karke reverse loop chalayenge
        for i in range(len(digits) - 1, -1, -1):
            # Agar digit 9 se kam hai, toh bas 1 add karo aur return kar do
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # Agar digit 9 hai, toh wo 0 ban jayega aur carry aage badhega
            digits[i] = 0
        
        # Agar loop poora khatam ho gaya, iska matlab saare digits 9 the (e.g., [9,9,9])
        # Ab array ke aage [1] jodna padega
        return [1] + digits