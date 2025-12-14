class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod, zero, one, two = 10**9+7, 0, 0, 1
        for c in corridor:
            if c == "S":
                zero = one
                one, two = two, one
            else:
                two = (two + zero) % mod
        
        return zero
