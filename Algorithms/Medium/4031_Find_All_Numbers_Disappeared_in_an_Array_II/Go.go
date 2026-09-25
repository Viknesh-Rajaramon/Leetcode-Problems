package main

func findDisappearedNumbers(nums []int, lower int, upper int) [][]int {
	result, nums_set, start := make([][]int, 0), make(map[int]bool), lower
	for _, num := range nums {
		nums_set[num] = true
	}

	for end := lower; end <= upper; end++ {
		if nums_set[end] {
			if start != end {
				result = append(result, []int{start, end - 1})
			}

			start = end + 1
		} else if end == upper {
			result = append(result, []int{start, end})
		}
	}

	return result
}
