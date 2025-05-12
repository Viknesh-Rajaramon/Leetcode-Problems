from imports import *

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_dict = {}
        n = len(nums)
        
        for i in range(n-1):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]
                if prod not in product_dict.keys():
                    product_dict[prod] = 0
                
                product_dict[prod] += 1

        no_of_tuples = 0
        for val in product_dict.values():
            if val > 1:
                no_of_tuples += val * (val - 1) * 4
        
        return no_of_tuples
