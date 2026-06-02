class Solution:
    def passwordStrength(self, password: str) -> int:
        result, chars = 0, set(password)
        for c in chars:
            if "a" <= c <= "z":
                result += 1
            elif "A" <= c <= "Z":
                result += 2
            elif "0" <= c <= "9":
                result += 3
            else:
                result += 5

        return result
