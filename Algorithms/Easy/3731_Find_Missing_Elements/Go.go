package main

func findMissingElements(nums []int) []int {
	result, set := make([]int, 0), make(map[int]struct{}, 0)
	min_, max_ := nums[0], nums[0]
	for _, num := range nums {
		set[num] = struct{}{}
		min_ = min(min_, num)
		max_ = max(max_, num)
	}

	for num := min_; num <= max_; num++ {
		if _, exists := set[num]; !exists {
			result = append(result, num)
		}
	}

	return result
}
