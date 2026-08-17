package main

func stoneGameV(stoneValue []int) int {
	n := len(stoneValue)
	dp, left, right := make([][]int, n), make([][]int, n), make([][]int, n)
	for i, val := range stoneValue {
		dp[i], left[i], right[i] = make([]int, n), make([]int, n), make([]int, n)
		left[i][i], right[i][i] = val, val
	}

	for start := n - 2; start >= 0; start-- {
		total_sum, split_at, left_sum := stoneValue[start], start, 0
		for end := start + 1; end < n; end++ {
			total_sum += stoneValue[end]
			for split_at <= end && 2*(left_sum+stoneValue[split_at]) <= total_sum {
				left_sum += stoneValue[split_at]
				split_at++
			}

			if left_sum*2 == total_sum {
				dp[start][end] = max(left[start][split_at-1], right[split_at][end])
			} else {
				if start == split_at {
					dp[start][end] = 0
					if split_at+1 <= end {
						dp[start][end] = right[split_at+1][end]
					}
				} else {
					dp[start][end] = 0
					if split_at-1 >= start {
						dp[start][end] = left[start][split_at-1]
					}

					if split_at+1 <= end {
						dp[start][end] = max(dp[start][end], right[split_at+1][end])
					}
				}
			}

			left[start][end] = max(left[start][end-1], total_sum+dp[start][end])
			right[start][end] = max(right[start+1][end], total_sum+dp[start][end])
		}
	}

	return dp[0][n-1]
}
