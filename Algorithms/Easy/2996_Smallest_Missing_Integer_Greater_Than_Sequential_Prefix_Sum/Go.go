package main

func missingInteger(nums []int) int {
	result, i := nums[0], 1
	for i < len(nums) && nums[i] == nums[i-1]+1 {
		result += nums[i]
		i++
	}

	num_set := make(map[int]bool)
	for _, num := range nums {
		num_set[num] = true
	}

	for num_set[result] {
		result += 1
	}

	return result
}
