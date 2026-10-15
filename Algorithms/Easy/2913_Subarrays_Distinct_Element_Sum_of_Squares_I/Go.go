package main

func sumCounts(nums []int) int {
	result, n := 0, len(nums)
	for i := range n {
		s := make(map[int]bool)
		for j := i; j < n; j++ {
			s[nums[j]] = true
			result += len(s) * len(s)
		}
	}

	return result
}
