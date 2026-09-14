package main

func maximumValue(n int, s int, m int) int64 {
	if n == 1 {
		return int64(s)
	}

	return int64(s + (n/2)*(m-1) + 1)
}
