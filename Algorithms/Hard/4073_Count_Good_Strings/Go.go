package main

func countGoodStrings(n int64) int {
	mod := int(1e9 + 7)
	var fib func(k int64) []int
	fib = func(k int64) []int {
		if k == 0 {
			return []int{0, 1}
		}

		f := fib(k >> 1)
		c := f[0] * ((2*f[1] - f[0] + mod) % mod) % mod
		d := ((f[0] * f[0] % mod) + (f[1] * f[1] % mod)) % mod
		if k&1 != 0 {
			return []int{d, (c + d) % mod}
		}

		return []int{c, d}
	}

	return (2 * fib(n)[0]) % mod
}
