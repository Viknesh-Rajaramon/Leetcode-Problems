package main

import (
	"math"
)

func maxPrimeSubset(n int, s int) []int {
	if n == 1 || s == 1 {
		return []int{}
	}

	is_prime := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		is_prime[i] = true
	}

	i := 2
	for i*i <= n {
		if is_prime[i] {
			for j := i * i; j <= n; j += i {
				is_prime[j] = false
			}
		}

		i++
	}

	primes := make([]int, 0)
	for prime := 2; prime <= n; prime++ {
		if is_prime[prime] {
			primes = append(primes, prime)
		}
	}

	n = len(primes)
	dp := make([][]int, n+1)
	for i := range n + 1 {
		dp[i] = make([]int, s+1)
		for j := range s + 1 {
			dp[i][j] = math.MaxInt
		}
	}

	dp[n][0] = 0
	for i := n - 1; i >= 0; i-- {
		for t := range s + 1 {
			best := dp[i+1][t]
			if t >= primes[i] && dp[i+1][t-primes[i]] != math.MaxInt && dp[i+1][t-primes[i]]+1 < best {
				best = dp[i+1][t-primes[i]] + 1
			}

			dp[i][t] = best
		}
	}

	target := 0
	for t := s; t > 0; t-- {
		if dp[0][t] != math.MaxInt {
			target = t
			break
		}
	}

	if target == 0 {
		return []int{}
	}

	result, need := make([]int, 0), dp[0][target]
	for i := range n {
		if need == 0 {
			break
		}

		if primes[i] <= target && dp[i+1][target-primes[i]] == need-1 {
			result = append(result, primes[i])
			target -= primes[i]
			need--
		}
	}

	return result
}
