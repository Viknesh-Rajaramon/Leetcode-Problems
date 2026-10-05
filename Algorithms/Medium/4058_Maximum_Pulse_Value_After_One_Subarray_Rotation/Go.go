package main

import (
	"math"
)

func maxValue(nums []int) int64 {
	n := len(nums)
	if n == 1 {
		return int64(nums[0])
	}

	result, even, odd, sum_ := int64(math.MaxInt64), int64(nums[0]), int64(0), int64(nums[0])
	for i := 1; i < n; i++ {
		if i%2 == 0 {
			sum_ += int64(nums[i])
			even = max(even, sum_)
			result = min(result, sum_-even)
		} else {
			sum_ -= int64(nums[i])
			odd = max(odd, sum_)
			result = min(result, sum_-odd)
		}
	}

	return sum_ - 2*result
}
