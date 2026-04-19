from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        result = 0
        for command in commands:
            if command == "UP":
                result -= n
            elif command == "DOWN":
                result += n
            elif command == "RIGHT":
                result += 1
            else:
                result -= 1
        
        return result
