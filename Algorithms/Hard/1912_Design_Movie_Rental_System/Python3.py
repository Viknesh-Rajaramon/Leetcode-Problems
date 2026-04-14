from typing import List

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = {}
        self.movie_price_shop = {}
        self.rented_movies = set()

        for shop, movie, price in entries:
            self.available[(shop, movie)] = price
            if movie not in self.movie_price_shop:
                self.movie_price_shop[movie] = []
            self.movie_price_shop[movie].append((price, shop))
        
        for movie in self.movie_price_shop:
            self.movie_price_shop[movie].sort()

    def search(self, movie: int) -> List[int]:
        result = []
        for _, shop in self.movie_price_shop.get(movie, []):
            if (shop, movie) not in self.rented_movies:
                result.append(shop)
                if len(result) == 5:
                    break
        
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented_movies.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented_movies.discard((shop, movie))

    def report(self) -> List[List[int]]:
        rented_list = []
        for shop, movie in self.rented_movies:
            price = self.available[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()
        return [[shop, movie] for _, shop, movie in rented_list[ : 5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
