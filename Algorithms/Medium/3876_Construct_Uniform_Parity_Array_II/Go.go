package main

import (
	"math"
)

func uniformArray(nums1 []int) bool {
	min_odd, min_even := math.MaxInt, math.MaxInt
	for _, num := range nums1 {
		if num%2 == 1 {
			min_odd = min(min_odd, num)
		} else {
			min_even = min(min_even, num)
		}
	}

	if min_odd == math.MaxInt || min_even == math.MaxInt {
		return true
	}

	return min_even > min_odd
}
