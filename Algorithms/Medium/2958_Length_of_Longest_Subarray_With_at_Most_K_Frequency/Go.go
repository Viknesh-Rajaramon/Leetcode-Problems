package main

func maxSubarrayLength(nums []int, k int) int {
	result, l, freq := 0, 0, make(map[int]int)
	for r, num := range nums {
		freq[num]++
		for freq[num] > k {
			freq[nums[l]]--
			l++
		}

		result = max(result, r-l+1)
	}

	return result
}
