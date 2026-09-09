package main

func isMiddleElementUnique(nums []int) bool {
	mid := len(nums) / 2
	for i := range len(nums) {
		if i == mid {
			continue
		}

		if nums[i] == nums[mid] {
			return false
		}
	}

	return true
}
