class Solution:
    def kthCharacter(self, k: int) -> str:
        result = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1

            k -= 1 << t
            result += 1
        
        return chr(ord("a") + result)
