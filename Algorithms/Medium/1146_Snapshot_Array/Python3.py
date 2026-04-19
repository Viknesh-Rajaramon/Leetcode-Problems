from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.record = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.record[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect_right(self.record[index], [snap_id, 10**9])
        return self.record[index][snap_index-1][1]



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
