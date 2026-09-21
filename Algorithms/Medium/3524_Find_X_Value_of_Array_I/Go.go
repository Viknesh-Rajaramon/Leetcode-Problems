package main

func resultArray(nums []int, k int) []int64 {
	result, dp := make([]int64, k), make([]int64, k)
	for _, num := range nums {
		new_dp := make([]int64, k)
		new_dp[num%k]++
		for r := range k {
			new_dp[(r*num)%k] += dp[r]
		}

		dp = new_dp
		for r := range k {
			result[r] += dp[r]
		}
	}

	return result
}
