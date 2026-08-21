class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        is_prime = bytearray([1]) * n
        is_prime[0] = is_prime[1] = 0
        
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                is_prime[p * p : n : p] = bytearray([0]) * len(is_prime[p * p : n : p])
                
        return sum(is_prime)