package main

func predictTheWinner(nums []int) bool {
	n := len(nums)
	if n%2 == 0 {
		return true
	}

	dp := make([]int, n)
	for i, num := range nums {
		dp[i] = num
	}

	for i := n - 2; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			dp[j] = max(nums[i]-dp[j], nums[j]-dp[j-1])
		}
	}

	return dp[n-1] >= 0
}
