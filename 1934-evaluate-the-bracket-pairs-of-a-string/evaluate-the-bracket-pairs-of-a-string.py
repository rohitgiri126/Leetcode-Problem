class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        res = []
        key = []
        in_bracket = False

        for ch in s:
            if ch == "(":
                in_bracket = True
            elif ch == ")":
                in_bracket = False
                res.append(d.get("".join(key), "?"))
                key.clear()
            elif in_bracket:
                key.append(ch)
            else:
                res.append(ch)

        return "".join(res)