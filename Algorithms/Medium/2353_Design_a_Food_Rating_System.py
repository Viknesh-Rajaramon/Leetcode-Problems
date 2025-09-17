from imports import *

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = (rating, cuisine)
            self.cuisine_map[cuisine].append((-rating, food))
        
        for cuisine in self.cuisine_map:
            heapify(self.cuisine_map[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        _, cuisine = self.food_map[food]
        self.food_map[food] = (newRating, cuisine)
        heappush(self.cuisine_map[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisine_map[cuisine][0][0] != -self.food_map[self.cuisine_map[cuisine][0][1]][0]:
            heappop(self.cuisine_map[cuisine])
        
        return self.cuisine_map[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
