class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        result, d, start = [], {key: value for key, value in knowledge}, -1
        for i, c in enumerate(s):
            if c == '(':
                start = i
            elif c == ')':
                result.append(d.get(s[start+1 : i], "?"))
                start = -1
            elif start < 0:
                result.append(c)
        
        return "".join(result)
