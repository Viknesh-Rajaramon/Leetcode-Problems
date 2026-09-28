class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        result = []
        for num in nums:
            curr, z = [], num // (1 << 25)
            if z:
                curr.append("z" * z)
                num %= (1 << 25)
            
            for i in range(24, -1, -1):
                if num & (1 << i):
                    curr.append(chr(97 + i))

            result.append("".join(curr))

        return result
