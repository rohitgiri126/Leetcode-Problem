class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        level = {s}
        while level:
            valid = [candidate for candidate in level if is_valid(candidate)]
            if valid:
                return valid
            level = {
                candidate[:i] + candidate[i + 1 :]
                for candidate in level
                for i in range(len(candidate))
                if candidate[i] in "()"
            }
        return [""]