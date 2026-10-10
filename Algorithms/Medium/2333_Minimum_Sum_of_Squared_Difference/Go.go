package main

import (
	"slices"
)

func minSumSquareDiff(nums1 []int, nums2 []int, k1 int, k2 int) int64 {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	diffs, k, total := make([]int64, 0), int64(k1+k2), int64(0)
	for i := range nums1 {
		num := int64(abs(nums1[i] - nums2[i]))
		diffs = append(diffs, num)
		total += num
	}

	if k >= total {
		return 0
	}

	slices.Sort(diffs)
	slices.Reverse(diffs)
	n, idx, count := len(diffs), 0, int64(0)
	for idx < n {
		curr := diffs[idx]
		for idx < n && diffs[idx] == curr {
			idx++
			count++
		}

		next_value := int64(0)
		if idx < n {
			next_value = diffs[idx]
		}

		needed := (curr - next_value) * count
		if k < needed {
			remainder, value := k%count, curr-k/count
			result := (count - remainder) * value * value
			result += remainder * (value - 1) * (value - 1)
			for i := idx; i < n; i++ {
				result += diffs[i] * diffs[i]
			}

			return result
		}

		k -= needed
	}

	return 0
}
