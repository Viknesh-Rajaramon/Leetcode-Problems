from bisect import bisect_left, bisect_right

class ExamTracker:
    def __init__(self):
        self.times = []
        self.pref_score = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.pref_score.append(self.pref_score[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        l, r = bisect_left(self.times, startTime), bisect_right(self.times, endTime)
        if l >= r:
            return 0
        
        total = self.pref_score[r] - self.pref_score[l]
        return total


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
