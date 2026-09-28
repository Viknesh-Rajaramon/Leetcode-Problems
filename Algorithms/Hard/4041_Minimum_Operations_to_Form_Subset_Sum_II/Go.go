package main

import (
	"math"
)

func minOperations(nums []int, sum int) int {
	get := func(m map[int]int, val, d int) int {
		if _, ok := m[val]; ok {
			return m[val]
		}

		return d
	}

	dp := make([]int, (sum + 1))
	for i := 1; i <= sum; i++ {
		dp[i] = math.MaxInt
	}

	for _, num := range nums {
		costs, value, divisions := make(map[int]int), num, 0
		for value > 0 {
			current, multiplications := value, 0
			for current <= sum {
				cost := divisions + multiplications
				if cost < get(costs, current, math.MaxInt) {
					costs[current] = cost
				}

				if current > (sum >> 1) {
					break
				}

				current <<= 1
				multiplications++
			}

			value >>= 1
			divisions++
		}

		next_dp := make([]int, (sum + 1))
		copy(next_dp, dp)
		for value, cost := range costs {
			for current_sum := range sum - value + 1 {
				if dp[current_sum] != math.MaxInt {
					candidate := dp[current_sum] + cost
					if candidate < next_dp[current_sum+value] {
						next_dp[current_sum+value] = candidate
					}
				}
			}
		}

		dp = next_dp
	}

	if dp[sum] == math.MaxInt {
		return -1
	}

	return dp[sum]
}
