class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9+7
        frequency = [0] * 26

        ord_a = ord("a")
        for c in s:
            frequency[ord(c) - ord_a] += 1
        
        for i in range(t):
            next_frequency = [0] * 26
            next_frequency[0] = frequency[25]
            next_frequency[1] = (frequency[25] + frequency[0]) % mod
            for j in range(2, 26):
                next_frequency[j] = frequency[j-1]

            frequency = next_frequency
            
        return sum(frequency) % mod
