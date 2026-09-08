class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        diff = [0] * (n+1)
        for i, v in enumerate(lights):
            if v == 0:
                continue
            
            diff[max(0, i-v)] += 1
            diff[min(n-1, i+v)+1] -= 1
        
        for i in range(n):
            diff[i+1] += diff[i]
        
        result, length = 0, 0
        for i in range(n):
            if diff[i] == 0:
                length += 1
            else:
                result += (length+2)//3
                length = 0

        result += (length+2)//3
        return result
