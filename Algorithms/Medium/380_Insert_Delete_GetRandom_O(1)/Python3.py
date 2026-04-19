import random

class RandomizedSet:

    def __init__(self):
        self.set = []
        self.set_map = {}

    def insert(self, val: int) -> bool:
        if self.set_map.get(val, -1) != -1:
            return False
        
        self.set_map[val] = len(self.set)
        self.set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if self.set_map.get(val, -1) == -1:
            return False
        
        index = self.set_map[val]
        element = self.set[-1]
        self.set[index] = element
        self.set_map[element] = index
        self.set.pop()
        self.set_map[val] = -1
        return True

    def getRandom(self) -> int:
        return random.choice(self.set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
