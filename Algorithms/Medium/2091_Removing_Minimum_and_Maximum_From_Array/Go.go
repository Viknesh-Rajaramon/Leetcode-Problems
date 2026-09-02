package main

func minimumDeletions(nums []int) int {
	n, min_idx, max_idx := len(nums), 0, 0
	for i, num := range nums {
		if num < nums[min_idx] {
			min_idx = i
		}

		if num > nums[max_idx] {
			max_idx = i
		}
	}

	l, r := min(min_idx, max_idx), max(min_idx, max_idx)
	return min(min(r+1, n-l), l+1+n-r)
}
