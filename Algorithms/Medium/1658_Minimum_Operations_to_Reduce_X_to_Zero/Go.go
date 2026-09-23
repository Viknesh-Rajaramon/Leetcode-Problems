package main

func minOperations(nums []int, x int) int {
	n, target := len(nums), -x
	for i := range n {
		target += nums[i]
	}

	if target < 0 {
		return -1
	}

	result, l, curr_sum := -1, 0, 0
	for r := range n {
		curr_sum += nums[r]
		for curr_sum > target {
			curr_sum -= nums[l]
			l++
		}

		if curr_sum == target {
			result = max(result, r-l+1)
		}
	}

	if result == -1 {
		return -1
	}

	return n - result
}
