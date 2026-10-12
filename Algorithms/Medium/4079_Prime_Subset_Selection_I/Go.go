package main

func maxPrimes(n int, s int) []int {
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

	result, total := make([]int, 0), 0
	for prime := 2; prime <= n; prime++ {
		if is_prime[prime] {
			if total+prime > s {
				break
			}

			total += prime
			result = append(result, prime)
		}
	}

	return result
}
