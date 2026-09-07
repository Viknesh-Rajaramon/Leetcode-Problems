package main

import (
	"math"
)

func maximumSum(nums []int, m int, l int, r int) int64 {
	n := len(nums)
	prefix := make([]int64, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + int64(nums[i])
	}

	type Pair struct {
		val int64
		pos int
	}

	result, dp := int64(math.MinInt64), make([]int64, n+1)
	for i := 1; i <= m; i++ {
		queue, new_dp := make([]Pair, 0), make([]int64, n+1)
		for i := 0; i <= n; i++ {
			new_dp[i] = math.MinInt64
		}

		for j := l * i; j <= n; j++ {
			k := j - l
			curr_val := dp[k] - prefix[k]
			for len(queue) > 0 && queue[len(queue)-1].val <= curr_val {
				queue = queue[:len(queue)-1]
			}

			queue = append(queue, Pair{val: curr_val, pos: k})
			if queue[0].pos < j-r {
				queue = queue[1:]
			}

			new_dp[j] = max(new_dp[j-1], queue[0].val+prefix[j])
		}

		result = max(result, new_dp[n])
		dp = new_dp
	}

	return result
}
