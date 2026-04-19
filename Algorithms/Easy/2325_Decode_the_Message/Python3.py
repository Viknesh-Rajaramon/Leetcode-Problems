class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_to_char = {}
        count = 0

        for c in key:
            if c != " " and c not in key_to_char:
                key_to_char[c] = chr(ord("a") + count)
                count += 1

        result = []
        for c in message:
            if c == " ":
                result.append(c)
            else:
                result.append(key_to_char[c])

        return "".join(result)
