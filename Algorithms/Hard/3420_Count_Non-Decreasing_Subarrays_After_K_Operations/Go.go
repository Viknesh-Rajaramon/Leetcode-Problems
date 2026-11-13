package main

import (
	"slices"
)

func countNonDecreasingSubarrays(nums []int, k int) int64 {
	result, n, stack, l, ops := int64(0), len(nums), make([]int, 0), 0, 0
	slices.Reverse(nums)
	for r := range n {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[r] {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			i := l - 1
			if len(stack) > 0 {
				i = stack[len(stack)-1]
			}

			ops += (nums[r] - nums[j]) * (j - i)
		}

		stack = append(stack, r)
		for ops > k {
			ops -= max(0, nums[stack[0]]-nums[l])
			if stack[0] == l {
				stack = stack[1:]
			}

			l++
		}

		result += int64(r - l + 1)
	}

	return result
}
