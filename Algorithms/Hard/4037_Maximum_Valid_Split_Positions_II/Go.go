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

	result, n := score(nums), len(nums)
	if n <= 2 {
		return result
	}

	g := 0
	for i := range n {
		if i > 0 && gcd(g, nums[i]) != g {
			result = max(result, score(slices.Concat(nums[:i], nums[i+1:])))
		}

		g = gcd(g, nums[i])
	}

	g = 0
	for i := n - 1; i >= 0; i-- {
		if i < n-1 && gcd(g, nums[i]) != g {
			result = max(result, score(slices.Concat(nums[:i], nums[i+1:])))
		}

		g = gcd(g, nums[i])
	}

	return result
}
