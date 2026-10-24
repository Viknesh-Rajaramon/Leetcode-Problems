class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def f(s: str) -> int:
            month, day = int(s[ : 2]), int(s[3 : ])
            return (275*month)//9 - 2*((month+9) // 12) + day - 30

        return max(0, min(f(leaveAlice), f(leaveBob)) - max(f(arriveAlice), f(arriveBob)) + 1)
