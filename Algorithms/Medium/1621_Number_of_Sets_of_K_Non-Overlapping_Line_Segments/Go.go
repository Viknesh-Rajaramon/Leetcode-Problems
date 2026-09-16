package main

func numberOfSets(n int, k int) int {
	mod := 1000000007

	var modPow func(base, exp int) int
	modPow = func(base, exp int) int {
		if exp == 0 {
			return 1
		}

		p := modPow(base, exp/2)
		p = (p * p) % mod
		if exp%2 == 0 {
			return p
		}

		return (p * (base % mod)) % mod
	}

	var nCr func(n, r int) int
	nCr = func(n, r int) int {
		if r < 0 || r > n {
			return 0
		}

		if r == 0 || r == n {
			return 1
		}

		r = min(r, n-r)
		if n < mod && r < mod {
			num, den := 1, 1
			for i := 1; i <= r; i++ {
				num = (num * (n + 1 - i)) % mod
				den = (den * i) % mod
			}

			return (num * modPow(den, mod-2)) % mod
		}

		return (nCr(n/mod, r/mod) * nCr(n%mod, r%mod)) % mod
	}

	return nCr(n+k-1, 2*k)
}
