from math import inf

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        result, p_0, m_0, p_1, m_1 = -inf, -inf, -inf, -inf, -inf
        for num in nums:
            np_0, nm_0, np_1, nm_1 = num, -inf, p_0, m_0
            if m_0 != -inf:
                np_0 = max(np_0, m_0 + num)
            
            if p_0 != -inf:
                nm_0 = p_0 - num
            
            if m_1 != -inf:
                np_1 = max(np_1, m_1 + num)
            
            if p_1 != -inf:
                nm_1 = max(nm_1, p_1 - num)
                
            p_0, p_1, m_0, m_1 = np_0, np_1, nm_0, nm_1
            result = max(result, p_1, m_1, m_0, p_0)
            
        return result
