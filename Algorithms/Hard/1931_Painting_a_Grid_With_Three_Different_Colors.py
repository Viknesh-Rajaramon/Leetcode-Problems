from collections import defaultdict

mod = 10**9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        valid = {}

        for mask in range(3**m):
            color = []
            mm = mask
            for i in range(m):
                color.append(mm % 3)
                mm //= 3
            
            if any(color[i] == color[i+1] for i in range(m-1)):
                continue
            
            valid[mask] = color
        
        neighbor = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    neighbor[mask1].append(mask2)
        
        result = [1 if mask in valid else 0 for mask in range(3**m)]
        for i in range(1, n):
            new_result = [0] * (3**m)
            for mask2 in valid.keys():
                for mask1 in neighbor[mask2]:
                    new_result[mask2] = (new_result[mask2] + result[mask1]) % mod
            
            result = new_result
        
        return sum(result) % mod
