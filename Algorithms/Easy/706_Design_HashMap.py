class MyHashMap:

    def __init__(self):
        self.hash_map = [[-1] * 1000 for _ in range(1000+1)]

    def put(self, key: int, value: int) -> None:
        hash1 = key // 1000
        hash2 = key % 1000
        self.hash_map[hash1][hash2] = value

    def get(self, key: int) -> int:
        hash1 = key // 1000
        hash2 = key % 1000
        return self.hash_map[hash1][hash2]

    def remove(self, key: int) -> None:
        hash1 = key // 1000
        hash2 = key % 1000
        self.hash_map[hash1][hash2] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
