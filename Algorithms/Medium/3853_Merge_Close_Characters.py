class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        result = ""
        for c in s:
            if len(result) >= k:
                if c not in result[-k : ]:
                    result += c
            elif c not in result:
                result += c

        return result
