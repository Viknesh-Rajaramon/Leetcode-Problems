class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        result, pre = [False] * n, [0] * n
        result[0] = True
        for i in range(minJump):
            pre[i] = 1
        
        for i in range(minJump, n):
            left = i-maxJump
            if s[i] == "0":
                total = pre[i-minJump] - (0 if left <= 0 else pre[left-1])
                result[i] = total != 0
            
            pre[i] = pre[i-1] + int(result[i])
        
        return result[n-1]
