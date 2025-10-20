from imports import *

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op[1] == "+":
                x += 1
            elif op[1] == "-":
                x -= 1

        return x
