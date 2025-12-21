from typing import List

class ATM:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.notes = [0] * len(self.denominations)

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        n = len(self.denominations)
        current = [0] * n

        for i in range(n-1, -1, -1):
            if self.notes[i] > 0:
                count = min(amount // self.denominations[i], self.notes[i])
                amount -= self.denominations[i] * count
                current[i] += count
            
        if amount == 0:
            for i in range(n):
                self.notes[i] -= current[i]
                
            return current
        
        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
