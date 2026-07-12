class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry == 1:
            # 1. Base sum start karo carry se
            total = carry

            # 2. Agar string 'a' me digits bachi hain, add karo
            if i >= 0:
                total += int(a[i])
                i -= 1

            # 3. Agar string 'b' me digits bachi hain, add karo
            if j >= 0:
                total += int(b[j])
                j -= 1

            # 4. Result me current bit daalo (0 ya 1)
            result.append(str(total % 2))

            # 5. Agle step ke liye carry nikalo (0 ya 1)
            carry = total // 2

        # Ulta karke jod do
        return "".join(result[::-1])