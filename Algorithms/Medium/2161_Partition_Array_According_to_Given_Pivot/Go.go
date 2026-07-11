package main

func pivotArray(nums []int, pivot int) []int {
	less, equal, more := make([]int, 0), make([]int, 0), make([]int, 0)
	for _, num := range nums {
		if num < pivot {
			less = append(less, num)
		} else if num > pivot {
			more = append(more, num)
		} else {
			equal = append(equal, num)
		}
	}

	result := make([]int, 0)
	result = append(result, less...)
	result = append(result, equal...)
	result = append(result, more...)

	return result
}
