class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total =  3 * 2**(n-1)
        if k > total:
            return ""
        
        letters = "abc"
        
        res = []
        left, right = 1, total
        
        for i in range(n):
            curr = left
            partition_size = (right - left + 1) // len(letters)

            for c in letters:
                if curr <= k < curr + partition_size:
                    res.append(c)
                    left = curr
                    right = curr + partition_size - 1
                    letters = "abc".replace(c, "")
                    break
                
                curr += partition_size

        return "".join(res)
