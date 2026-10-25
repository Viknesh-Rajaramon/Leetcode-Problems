package main

func countSubarrays(nums []int, minK int, maxK int) int64 {
	result, l := int64(0), 0
	for r := range nums {
		if nums[r] < minK || nums[r] > maxK {
			l = r + 1
		} else {
			result += int64(r - l + 1)
		}
	}

	return result
}
