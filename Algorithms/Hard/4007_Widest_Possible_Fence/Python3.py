class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        freq, height, values = {}, {}, []
        for plank in planks:
            if plank not in freq:
                freq[plank] = 0
            
            freq[plank] += 1

        for key in freq:
            height[key] = freq[key]
            values.append(key)
        
        n = len(values)
        for i in range(n):
            a = values[i]
            for j in range(i, n):
                b = values[j]
                h = a+b
                if h not in height:
                    height[h] = 0
                
                height[h] += (freq[a] // 2 if a == b else min(freq[a], freq[b]))
        
        result = 0
        for h in height:
            result = max(result, height[h])
        
        return result
