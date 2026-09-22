class Solution:
    def kthDigit(self, k: int) -> int:
        if k < 10:
            return k
        
        d = 1
        while k > 9 * d * (10**(d-1)):
            k -= 9 * d * (10**(d-1))
            d += 1
        
        b, pos = 10**(d-2) + ((k-1)//(10*d)), (k-1) % (10*d)
        num_idx = pos // d
        if b%2 == 1:
            num_idx = 9 - num_idx
        
        return int(str(10*b + num_idx)[pos % d])
