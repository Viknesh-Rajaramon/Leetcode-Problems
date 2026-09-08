package main

func countValidSubarrays(nums []int, x int) int {
	result, n := 0, len(nums)
	prefix := make([]int, n+1)
	for i := range n {
		prefix[i+1] = prefix[i] + nums[i]
	}

	for i := range n {
		for j := i; j < n; j++ {
			total := prefix[j+1] - prefix[i]
			if total%10 != x {
				continue
			}

			for total >= 10 {
				total /= 10
			}

			if total == x {
				result++
			}
		}
	}

	return result
}
