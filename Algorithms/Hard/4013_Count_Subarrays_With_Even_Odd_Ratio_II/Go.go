package main

import (
	"slices"
)

func countRatioSubarrays(nums []int, a int, b int) int64 {
	bisect_right := func(arr []int, x int) int {
		low, high := 0, len(arr)-1
		for low <= high {
			mid := (low + high) >> 1
			if arr[mid] <= x {
				low = mid + 1
			} else {
				high = mid - 1
			}
		}

		return low
	}

	result, pre, x := int64(0), 0, []int{0}
	for _, num := range nums {
		if num%2 == 1 {
			pre += a
		} else {
			pre -= b
		}

		i := bisect_right(x, pre)
		x = slices.Insert(x, i, pre)
		result += int64(i)
	}

	return result
}
