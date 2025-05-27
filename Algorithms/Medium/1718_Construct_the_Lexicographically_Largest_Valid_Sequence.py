from imports import *

class Solution:
    def generateSeq(self, seq: List[int], used: List[bool], index: int, n: int) -> bool:
        seq_len = len(seq)
        if index == seq_len:
            return True
        
        if seq[index] != 0:
            return self.generateSeq(seq, used, index+1, n)
        
        for num in range(n, 0, -1):
            next_index = index if num == 1 else index + num

            if used[num-1] or (num > 1 and (next_index >= seq_len or seq[next_index] != 0)):
                continue
            
            seq[index] = num
            seq[next_index] = num
            used[num-1] = True

            if self.generateSeq(seq, used, index+1, n):
                return True
            
            seq[index] = 0
            seq[next_index] = 0
            used[num-1] = False
        
        return False

    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [0] * (2*n-1)
        used = [False] * n
        self.generateSeq(seq, used, 0, n)
        return seq
