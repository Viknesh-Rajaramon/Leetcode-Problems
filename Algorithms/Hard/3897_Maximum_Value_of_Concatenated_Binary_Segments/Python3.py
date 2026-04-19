class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        mod, mix, ones, zeroes = 10**9+7, [], 0, 0
        for o, z in zip(nums1, nums0):
            if z == 0:
                ones += o
            elif o == 0:
                zeroes += z
            else:
                mix.append((-o, z))
        
        result = "1"*ones
        for o, z in sorted(mix):
            result += "1"*-o + "0"*z

        return int(result + "0"*zeroes, 2) % mod
