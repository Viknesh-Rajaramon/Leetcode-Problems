package main

import (
	"slices"
)

func maxValidSplits(nums []int) int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	score := func(arr []int) int {
		m := len(arr)
		if m == 1 {
			return 0
		}

		suffix := make([]int, m)
		suffix[len(suffix)-1] = arr[m-1]
		for i := m - 2; i >= 0; i-- {
			suffix[i] = gcd(suffix[i+1], arr[i])
		}

		ans, left_gcd := 0, 0
		for i := range m - 1 {
			left_gcd = gcd(left_gcd, arr[i])
			if left_gcd == suffix[i+1] {
				ans++
			}
		}

		return ans
	}

	result := score(nums)
	for i := range nums {
		result = max(result, score(slices.Concat(nums[:i], nums[i+1:])))
	}

	return result
}
