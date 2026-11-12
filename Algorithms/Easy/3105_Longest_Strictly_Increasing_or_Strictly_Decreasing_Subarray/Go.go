package main

func longestMonotonicSubarray(nums []int) int {
	result, inc, dec := 1, 1, 1
	for i := range len(nums) - 1 {
		if nums[i] < nums[i+1] {
			inc++
			dec = 1
		} else if nums[i] > nums[i+1] {
			dec++
			inc = 1
		} else {
			inc = 1
			dec = 1
		}

		result = max(result, inc, dec)
	}

	return result
}
