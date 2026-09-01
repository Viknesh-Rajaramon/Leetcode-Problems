class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        
        result, left, count = s, 0, 0
        for right, c in enumerate(s):
            count += int(c)
            while count > k or s[left] == "0":
                count -= int(s[left])
                left += 1
            
            if count < k:
                continue
                
            if right+1-left < len(result) or right+1-left == len(result) and s[left : right+1] < result:
                result = s[left: right+1]

        return result
