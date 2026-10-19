package main

func minDeletions(nums []int) int {
	result := 0
	for i := range len(nums) - 1 {
		if nums[i]^nums[i+1] == 0 {
			result++
		}
	}

	return result
}
