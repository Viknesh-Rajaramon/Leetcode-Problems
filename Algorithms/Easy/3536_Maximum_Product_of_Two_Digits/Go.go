package main

func maxProduct(n int) int {
	first, second := 0, 0
	for n > 0 {
		digit := n % 10
		n /= 10
		if digit > first {
			second = first
			first = digit
		} else if digit > second {
			second = digit
		}
	}

	return first * second
}
