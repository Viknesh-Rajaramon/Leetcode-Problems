package main

func sumOfSquares(nums []int) int {
	result, n := 0, len(nums)
	for i := range n {
		if n%(i+1) == 0 {
			result += nums[i] * nums[i]
		}
	}

	return result
}
