package main

func threeFibonacciSum(n int) bool {
	f_0, f_1, f_2 := 0, 1, 1
	for f_0+f_1+f_2 <= n {
		if f_0+f_1+f_2 == n {
			return true
		}

		f_0 = f_1
		f_2 += f_1
		f_1 = f_2 - f_1
	}

	return false
}
