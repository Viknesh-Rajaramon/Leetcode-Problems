class Solution:
    def toHex(self, num: int) -> str:
        hex_chars = {i: str(c) for i, c in enumerate(list(range(10)) + ["a", "b", "c", "d", "e", "f"])}
        
        x = num
        if x < 0:
            x = (2**32 + x) % 2**32
        
        result = []
        while True:
            result.append(hex_chars[x % 16])
            x //= 16

            if x == 0:
                break
        
        if num < 0:
            result.append("f" * (8 - len(result)))
        
        return "".join(result[::-1])
