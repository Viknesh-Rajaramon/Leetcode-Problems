package main

import (
	"math"
)

func divisibleGame(nums []int) int {
	mod, n, max_val := int(1e9+7), len(nums), 0
	prefix := make([]int, n+1)
	for i := range n {
		prefix[i+1] = prefix[i] + nums[i]
		max_val = max(max_val, nums[i])
	}

	if prefix[n] == n {
		return mod - 2
	}

	spf := make([]int, max_val+1)
	for i := range max_val + 1 {
		spf[i] = i
	}

	for i := 2; i*i <= max_val; i++ {
		if spf[i] == i {
			for j := i * i; j <= max_val; j += i {
				if spf[j] == j {
					spf[j] = i
				}
			}
		}
	}

	mix, max_diff, best_k := make([]int, max_val+1), math.MinInt, 0
	for i, num := range nums {
		x := num
		for x > 1 {
			p := spf[x]
			diff := max(0, mix[p]-prefix[i]) + num
			if diff > max_diff || (diff == max_diff && p < best_k) {
				max_diff, best_k = diff, p
			}

			mix[p] = diff + prefix[i+1]
			for x%p == 0 {
				x /= p
			}
		}
	}

	return max_diff * best_k % mod
}
