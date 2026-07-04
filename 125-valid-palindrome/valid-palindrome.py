class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. खाली स्ट्रिंग बनाई
        clean_str = ""
        
        # 2. लूप चलाकर सिर्फ alphanumeric कैरेक्टर्स को lowercase में जोड़ा
        for ch in s:
            if ch.isalnum():
                x = ch.lower()
                clean_str += x  # यहाँ .append() की जगह += का यूज़ किया
                
        # 3. साफ़ की हुई स्ट्रिंग को उसके रिवर्स से कम्पेयर किया
        if clean_str == clean_str[::-1]:
            return True   # Python में T हमेशा Capital (True) होगा
        return False      # Python में F हमेशा Capital (False) होगा