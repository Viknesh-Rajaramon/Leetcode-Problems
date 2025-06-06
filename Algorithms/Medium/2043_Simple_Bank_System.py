from imports import *

class Bank:

    def __init__(self, balance: List[int]):
        self.balances = balance
        self.n = len(self.balances)
    
    def _accountExists(self, account: int) -> bool:
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self._accountExists(account1) and self._accountExists(account2)):
            return False
        
        if not self.withdraw(account1, money):
            return False
        
        return self.deposit(account2, money)

    def deposit(self, account: int, money: int) -> bool:
        if not self._accountExists(account):
            return False
        
        self.balances[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._accountExists(account) or self.balances[account-1] < money:
            return False
        
        self.balances[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
