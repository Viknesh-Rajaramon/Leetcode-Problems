class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        result, gains = 0, []
        for num in nums:
            result += num
            freq, x = [0] * 10, num
            while x > 0:
                freq[x%10] += 1
                x //= 10
            
            max_num = 0
            for d in range(9, -1, -1):
                for _ in range(freq[d]):
                    max_num = max_num*10 + d
            
            if max_num > num:
                gains.append(max_num - num)

        gains.sort(reverse = True)
        for i in range(min(k, len(gains))):
            result += gains[i]
        
        return result
