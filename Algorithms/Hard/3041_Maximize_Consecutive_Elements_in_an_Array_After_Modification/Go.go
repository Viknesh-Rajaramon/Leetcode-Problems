package main

import (
	"sort"
)

func maxSelectedElements(nums []int) int {
	sort.Ints(nums)
	result, dp := 0, make(map[int]int)
	for _, num := range nums {
		dp[num+1], dp[num] = dp[num]+1, dp[num-1]+1
		result = max(result, dp[num+1], dp[num])
	}

	return result
}
