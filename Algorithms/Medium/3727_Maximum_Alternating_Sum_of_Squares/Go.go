package main

import (
	"slices"
)

func maxAlternatingSum(nums []int) int64 {
	n := len(nums)
	squares := make([]int64, n)
	for i, num := range nums {
		squares[i] = int64(num * num)
	}

	slices.Sort(squares)
	slices.Reverse(squares)
	result, k := int64(0), (n+1)/2
	for i, num := range squares {
		if i < k {
			result += num
		} else {
			result -= num
		}
	}

	return result
}
