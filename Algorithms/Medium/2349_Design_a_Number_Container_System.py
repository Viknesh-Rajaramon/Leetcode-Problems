from imports import *

class NumberContainers:

    def __init__(self):
        self.index_num = {}
        self.num_index = {}

    def change(self, index: int, number: int) -> None:
        self.index_num[index] = number

        if number not in self.num_index:
            self.num_index[number] = []
        
        heappush(self.num_index[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_index:
            return -1
        
        indices = self.num_index[number]
        while indices:
            min_index = indices[0]

            if self.index_num[min_index] == number:
                return min_index
            
            heappop(indices)
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
