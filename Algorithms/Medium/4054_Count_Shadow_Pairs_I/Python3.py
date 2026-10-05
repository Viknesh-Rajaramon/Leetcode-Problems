class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        result, total, stack = 0, 0, []
        for num in nums:
            while stack and num < stack[-1][0]:
                total -= stack[-1][1]
                stack.pop()
            
            if stack:
                result += total
                if stack[-1][0] == num:
                    result -= stack[-1][1]
                    stack[-1][1] += 1
                else:
                    stack.append([num, 1])    
            else:
                stack.append([num, 1])
            
            total += 1
        
        return result
