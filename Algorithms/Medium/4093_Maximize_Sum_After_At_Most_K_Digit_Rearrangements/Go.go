package main

import (
	"slices"
)

func maximizeSum(nums []int, k int) int64 {
	result, gains := int64(0), make([]int64, 0)
	for _, num := range nums {
		result += int64(num)
		freq, x := make([]int, 10), num
		for x > 0 {
			freq[x%10]++
			x /= 10
		}

		max_num := 0
		for d := 9; d >= 0; d-- {
			for range freq[d] {
				max_num = max_num*10 + d
			}
		}

		if max_num > num {
			gains = append(gains, int64(max_num-num))
		}
	}

	slices.Sort(gains)
	slices.Reverse(gains)
	for i := range min(k, len(gains)) {
		result += gains[i]
	}

	return result
}
