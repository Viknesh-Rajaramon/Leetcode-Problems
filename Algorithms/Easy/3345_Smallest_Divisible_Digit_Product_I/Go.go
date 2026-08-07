package main

func smallestNumber(n int, t int) int {
	for range 10 {
		product := 1
		for x := n; x > 0; x /= 10 {
			product *= x % 10
		}

		if product%t == 0 {
			return n
		}

		n++
	}

	return n
}
