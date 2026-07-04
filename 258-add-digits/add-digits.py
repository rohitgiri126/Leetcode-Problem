class Solution:
    def addDigits(self, num: int) -> int:
        # जब तक नंबर 9 से बड़ा है (यानी single digit नहीं बना)
        while num > 9:
            digit_sum = 0
            # नंबर के सारे डिजिट्स को आपस में जोड़ो
            while num > 0:
                digit_sum += num % 10  # आखिरी डिजिट निकाला और जोड़ा
                num = num // 10        # आखिरी डिजिट को हटाया
            
            # अब num को नए सम (sum) से अपडेट कर दो
            num = digit_sum
            
        return num