package main

func minSumOfLengths(arr []int, target int) int {
	result, n, total := len(arr)+1, len(arr), 0
	dp, l := make([]int, n+1), 0
	for i := range dp {
		dp[i] = n
	}

	for r, num := range arr {
		total += num
		for total > target {
			total -= arr[l]
			l++
		}

		dp[r+1] = dp[r]
		if total == target {
			result = min(result, r-l+1+dp[l])
			dp[r+1] = min(dp[r], r-l+1)
		}
	}

	if result == n+1 {
		return -1
	}

	return result
}
