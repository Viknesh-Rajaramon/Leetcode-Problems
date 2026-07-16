package main

import (
	"sort"
)

func gcdSum(nums []int) int64 {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	curr_max, prefix_gcd := 0, make([]int, 0)
	for _, num := range nums {
		curr_max = max(curr_max, num)
		prefix_gcd = append(prefix_gcd, gcd(num, curr_max))
	}

	sort.Ints(prefix_gcd)
	result, left, right := 0, 0, len(nums)-1
	for left < right {
		result += gcd(prefix_gcd[left], prefix_gcd[right])
		left += 1
		right -= 1
	}

	return int64(result)
}
