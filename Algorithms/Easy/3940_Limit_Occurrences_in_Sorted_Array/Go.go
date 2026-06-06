package main

func limitOccurrences(nums []int, k int) []int {
	i := 0
	for _, num := range nums {
		if i < k || num != nums[i-k] {
			nums[i] = num
			i += 1
		}
	}

	return nums[:i]
}
