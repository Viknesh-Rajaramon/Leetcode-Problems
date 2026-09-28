package main

func minOperations(nums []int, sum int) int {
	dp, Max := make([]int, sum+1), int(1e9+7)
	for i := 1; i <= sum; i++ {
		dp[i] = Max
	}

	for _, num := range nums {
		new_dp := make([]int, sum+1)
		copy(new_dp, dp)
		n, count := num, 0
		for n > 0 {
			for i := sum; i >= n; i-- {
				new_dp[i] = min(new_dp[i], dp[i-n]+count)
			}

			count++
			n >>= 1
		}

		n, count = num<<1, 1
		for n <= sum {
			for i := sum; i >= n; i-- {
				new_dp[i] = min(new_dp[i], dp[i-n]+count)
			}

			count++
			n <<= 1
		}

		dp = new_dp
	}

	if dp[sum] == Max {
		return -1
	}

	return dp[sum]
}
