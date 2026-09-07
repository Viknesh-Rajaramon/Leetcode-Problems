package main

func sumOfGoodIntegers(n int, k int) int {
	result := 0
	for x := max(1, n-k); x <= n+k; x++ {
		if n&x == 0 {
			result += x
		}
	}

	return result
}
