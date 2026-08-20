package main

func resultArray(nums []int) []int {
	n := len(nums)
	result := make([]int, n)
	result[0], result[n-1] = nums[0], nums[1]
	idx, rev_idx := 0, n-1
	for i := 2; i < n; i++ {
		if result[idx] > result[rev_idx] {
			idx++
			result[idx] = nums[i]
		} else {
			rev_idx--
			result[rev_idx] = nums[i]
		}
	}

	l, r := rev_idx, n-1
	for l < r {
		result[l], result[r] = result[r], result[l]
		l++
		r--
	}

	return result
}
