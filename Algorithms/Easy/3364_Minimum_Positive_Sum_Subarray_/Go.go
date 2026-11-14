package main

import (
	"math"
)

func minimumSumSubarray(nums []int, l int, r int) int {
	n := len(nums)
	prefix_sum := make([]int, n+1)
	for i := range n {
		prefix_sum[i+1] = prefix_sum[i] + nums[i]
	}

	result := math.MaxInt
	for length := l; length <= min(r, n); length++ {
		for start := 0; start <= n-length; start++ {
			total := prefix_sum[start+length] - prefix_sum[start]
			if total > 0 {
				result = min(result, total)
			}
		}
	}

	if result != math.MaxInt {
		return result
	}

	return -1
}
