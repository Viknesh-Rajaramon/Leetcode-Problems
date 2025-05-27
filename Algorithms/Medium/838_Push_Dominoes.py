class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        result = [0] * n

        force = 0
        for i in range(n):
            if dominoes[i] == "L":
                force = 0
            elif dominoes[i] == "R":
                force = n
            else:
                force = max(force - 1, 0)
            
            result[i] += force
        
        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == "L":
                force = n
            elif dominoes[i] == "R":
                force = 0
            else:
                force = max(force - 1, 0)
            
            result[i] -= force
        
        return "".join("." if res == 0 else "R" if res > 0 else "L" for res in result)
