class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        stack = [[] for _ in range(26)]
        
        ord_a = ord("a")
        for i in range(n):
            if s[i] != "*":
                stack[ord(s[i]) - ord_a].append(i)
            else:
                for st in stack:
                    if st:
                        st.pop()
                        break
        
        result = [""] * n
        for i in range(26):
            for j in stack[i]:
                result[j] = chr(i + ord_a)
        
        return "".join(result)
