package main

func peakValleyDifference(nums []int) int {
	result := 0
	for i := 1; i < len(nums)-1; i++ {
		if nums[i] > nums[i-1] && nums[i] > nums[i+1] {
			result += nums[i]
		}

		if nums[i] < nums[i-1] && nums[i] < nums[i+1] {
			result -= nums[i]
		}
	}

	return result
}
