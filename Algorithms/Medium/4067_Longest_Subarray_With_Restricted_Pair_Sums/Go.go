package main

func maxSubarray(nums []int) int {
	result, n, l, count := 0, len(nums), 0, make([]int, 501)
	is_valid := func(target int) bool {
		for i := 1; i <= target/2; i++ {
			if 2*i == target {
				if count[i] >= 2 {
					return false
				}
			} else {
				if count[i] > 0 && count[target-i] > 0 {
					return false
				}
			}
		}

		for i := 1; i < 501-target; i++ {
			if count[i] > 0 && count[i+target] > 0 {
				return false
			}
		}

		return true
	}

	for r := range n {
		for !is_valid(nums[r]) {
			count[nums[l]]--
			l++
		}

		count[nums[r]]++
		result = max(result, r-l+1)
	}

	return result
}
