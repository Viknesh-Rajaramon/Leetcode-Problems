package main

func longestSubarray(nums []int, k int) int {
	result, n := 0, len(nums)
	for l := range n {
		curr_sum, seen := 0, make(map[int]bool)
		for r := l; r < n; r++ {
			curr_sum += nums[r]
			seen[((2*nums[r]%k)+k)%k] = true
			target := ((curr_sum % k) + k) % k
			if target == 0 || seen[target] {
				result = max(result, r-l+1)
			}
		}
	}

	return result
}
