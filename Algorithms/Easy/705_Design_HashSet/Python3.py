class MyHashSet:

    def __init__(self):
        self.hash_set = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        
        hash = key % 1000
        self.hash_set[hash].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            hash = key % 1000
            self.hash_set[hash].remove(key)

    def contains(self, key: int) -> bool:
        hash = key % 1000
        for k in self.hash_set[hash]:
            if k == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
