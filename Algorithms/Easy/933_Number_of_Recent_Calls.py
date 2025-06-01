class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        
        low, high = 0, len(self.counter) - 1 
        while low < high:
            mid = (low+high) // 2

            if self.counter[mid] >= t - 3000:
                high = mid
            else:
                low = mid + 1

        return len(self.counter) - low


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
