class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        values = sorted(set(nums))
        n = len(values)
        if n == 1:
            return 0

        ranks = {value: i for i, value in enumerate(values)}
        tasks = [([ranks[value] for value in nums], 0, n-1)]
        result = 0
        while tasks:
            sequence, low, high = tasks.pop()
            mid, left, right, stack, caps, starts = (low+high) >> 1, [], [], [], [], []
            for x in sequence:
                if x <= mid:
                    left.append(x)
                    while stack and stack[-1] < x:
                        stack.pop()

                    size = len(stack)
                    while starts and starts[-1] >= size:
                        starts.pop()
                        caps.pop()

                    stack.append(x)
                    if not caps or caps[-1] != n:
                        caps.append(n)
                        starts.append(size)
                else:
                    right.append(x)
                    if caps and caps[-1] >= x:
                        start = starts.pop()
                        caps.pop()
                        while caps and caps[-1] >= x:
                            start = starts.pop()
                            caps.pop()

                        result += len(stack) - start
                        caps.append(x)
                        starts.append(start)

            if low < mid and len(left) > 1:
                tasks.append((left, low, mid))
            
            if mid+1 < high and len(right) > 1:
                tasks.append((right, mid+1, high))

        return result
