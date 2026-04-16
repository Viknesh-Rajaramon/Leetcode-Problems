class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        result, n_len, digits = 0, len(str(n)), list(map(int, str(n)[::-1]))
        for a_len in range(n_len):
            for b_len in range(n_len):
                dp = [1, 0]

                for pos in range(n_len):
                    new_dp = [0, 0]

                    a_range = range(1, 10) if pos <= a_len else (0, )
                    b_range = range(1, 10) if pos <= b_len else (0, )

                    for carry in (0, 1):
                        if dp[carry] == 0:
                            continue
                        
                        for i in a_range:
                            for j in b_range:
                                sum_ = i + j + carry
                                if sum_ % 10 == digits[pos]:
                                    new_dp[sum_ // 10] += dp[carry]
                    
                    dp = new_dp
                
                result += dp[0]

        return result
