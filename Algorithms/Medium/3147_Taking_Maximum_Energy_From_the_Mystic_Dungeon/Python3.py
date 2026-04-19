from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        result = max(energy[n-k : ])
        for i in range(n-1-k, -1, -1):
            energy[i] += energy[i+k]
            if result < energy[i]:
                result = energy[i]
        
        return result
