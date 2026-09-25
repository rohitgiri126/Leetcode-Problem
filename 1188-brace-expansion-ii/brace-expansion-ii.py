class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = [[]]

        for char in expression:
            if char.isalpha():
                stack[-1].append({char})
            elif char == "{":
                stack.append([])
            elif char == ",":
                stack[-1].append(",")
            elif char == "}":
                group = stack.pop()
                res = set()
                cur = [{""}]
                for item in group:
                    if item == ",":
                        for prod in cur:
                            res.update(prod)
                        cur = [{""}]
                    else:
                        cur = [{a + b for a in prod for b in item} for prod in cur]
                for prod in cur:
                    res.update(prod)
                stack[-1].append(res)

        res = set()
        cur = [{""}]
        for item in stack[0]:
            if item == ",":
                for prod in cur:
                    res.update(prod)
                cur = [{""}]
            else:
                cur = [{a + b for a in prod for b in item} for prod in cur]
        for prod in cur:
            res.update(prod)

        return sorted(res)