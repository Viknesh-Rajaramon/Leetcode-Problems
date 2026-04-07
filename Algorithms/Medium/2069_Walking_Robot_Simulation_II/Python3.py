from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = 0
        self.moved = False
        self.perimeter = 2 * (width + height - 2)

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        if self.pos < self.width:
            return [self.pos, 0]
        
        if self.pos < self.width + self.height - 1:
            return [self.width - 1, self.pos - self.width + 1]

        if self.pos < 2*self.width + self.height - 2:
            return [2*self.width + self.height - 3 - self.pos, self.height - 1]
        
        return [0, self.perimeter - self.pos]

    def getDir(self) -> str:
        if self.pos == 0:
            return "South" if self.moved else "East"
        
        if self.pos < self.width:
            return "East"
        
        if self.pos < self.width + self.height - 1:
            return "North"
        
        if self.pos < 2*self.width + self.height - 2:
            return "West"
        
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
