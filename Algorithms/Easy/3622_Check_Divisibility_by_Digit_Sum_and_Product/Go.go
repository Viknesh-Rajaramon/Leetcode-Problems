package main

func checkDivisibility(n int) bool {
	sum_, product_ := 0, 1
	for x := n; x > 0; x /= 10 {
		r := x % 10
		sum_ += r
		product_ *= r
	}

	return n%(sum_+product_) == 0
}
