from imports import *

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = (100 - discount) / 100
        self.products_prices = {product: price for product, price in zip(products, prices)}
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        bill = 0

        for p, a in zip(product, amount):
            bill += a * self.products_prices[p]

        if self.count == self.n:
            self.count = 0
            return bill * self.discount

        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
