package main

import (
	"math"
	"slices"
)

func longestSubarray(nums []int, k int) int {
	M := slices.Max(nums)
	spf := make([]int, M+1)
	for i := range M + 1 {
		spf[i] = i
	}

	for i := 2; i <= int(math.Sqrt(float64(M))); i++ {
		if spf[i] == i {
			for j := i * i; j <= M; j += i {
				if spf[j] == j {
					spf[j] = i
				}
			}
		}
	}

	prime_factors := func(x int) map[int]bool {
		factors := make(map[int]bool)
		for x > 1 {
			p := spf[x]
			factors[p] = true
			for x%p == 0 {
				x /= p
			}
		}

		return factors
	}

	result, l, freq := 0, 0, make(map[int]int)
	for r := range nums {
		for p := range prime_factors(nums[r]) {
			freq[p]++
		}

		for len(freq) > k {
			for p := range prime_factors(nums[l]) {
				freq[p]--
				if freq[p] == 0 {
					delete(freq, p)
				}
			}

			l++
		}

		result = max(result, r-l+1)
	}

	return result
}
