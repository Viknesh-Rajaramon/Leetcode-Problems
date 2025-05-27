class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        
        min_count = 0
        for i in range(k):
            if blocks[i] == "W":
                min_count += 1
        
        count = min_count
        for i in range(k, n):
            if blocks[i] == "W":
                count += 1
            
            if blocks[i-k] == "W":
                count -= 1
            
            min_count = min(min_count, count)
        
        return min_count
