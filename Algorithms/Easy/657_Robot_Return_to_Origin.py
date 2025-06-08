class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_map = {"L": 0, "R": 0, "U": 0, "D": 0}
        for m in moves:
            move_map[m] += 1
        
        return move_map["L"] == move_map["R"] and move_map["U"] == move_map["D"]
