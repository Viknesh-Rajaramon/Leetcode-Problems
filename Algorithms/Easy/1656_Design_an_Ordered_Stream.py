from imports import *

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * 1000
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        
        result = []
        while self.stream[self.ptr] != "":
            result.append(self.stream[self.ptr])
            self.ptr += 1
        
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
