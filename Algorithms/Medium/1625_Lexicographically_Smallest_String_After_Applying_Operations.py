class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n, increment, seen = len(s), {str(d): str((d+a) % 10) for d in range(10)}, set()
        def dfs(s: str) -> None:
            if s in seen:
                return
            
            seen.add(s)
            dfs("".join([s[i] if i % 2 == 0 else increment[s[i]] for i in range(n)]))
            dfs(s[n-b : ] + s[ : n-b])
        
        dfs(s)
        return min(seen)
