package main

func checkGoodInteger(n int) bool {
	result := 0
	for n > 0 && result < 50 {
		d := n % 10
		result += d * (d - 1)
		n /= 10
	}

	return result >= 50
}
