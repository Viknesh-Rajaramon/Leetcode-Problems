package main

func countGoodRotations(nums []int) int {
	n := len(nums)
	result, mid, half, total := 0, n/2, 0, 0
	for i := range mid {
		half += nums[i]
	}

	for i := range n {
		total += nums[i]
	}

	for i := range n {
		if 2*half > total {
			result++
		}

		half -= nums[i]
		half += nums[(mid+i)%n]
	}

	return result
}
