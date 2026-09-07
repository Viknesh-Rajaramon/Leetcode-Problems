class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        result = []
        def dfs(prev: str, cost: int, path: str):
            if cost > k:
                return
            
            if len(path) == n:
                result.append(path)
                return
            
            dfs("0", cost, path+"0")
            if prev != "1":
                dfs("1", cost+len(path), path+"1")

        dfs("0", 0, "")
        return result
