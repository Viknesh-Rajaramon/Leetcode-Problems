class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n, freq = len(s), [0] * 26
        for c in s:
            freq[ord(c) - ord("a")] += 1

        result, temp = None, []
        def dfs(pos: int, found: bool) -> None:
            nonlocal result
            if result is not None:
                return

            if pos == n:
                candidate = "".join(temp)
                if candidate > target:
                    result = candidate
                
                return
            
            start = 0 if found else ord(target[pos]) - ord("a")
            for i in range(start, 26):
                if freq[i]:
                    freq[i] -= 1
                    temp.append(chr(ord("a") + i))
                    dfs(pos+1, found or i > ord(target[pos]) - ord("a"))
                    temp.pop()
                    freq[i] += 1
        
        dfs(0, False)
        return result if result else ""
