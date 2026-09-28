package main

func sumDecoded(nums []int64) int {
	mod := int(1e9 + 7)
	power_mod := func(base, exp int) int {
		result := 1
		for exp > 0 {
			if (exp & 1) != 0 {
				result = ((result % mod) * (base % mod)) % mod
			}

			base = (base * base) % mod
			exp >>= 1
		}

		return result
	}

	result := 0
	for _, num := range nums {
		width, d, digits := int(num%10), int(num/10), 0
		v := d
		for v > 0 {
			digits++
			v /= 10
		}

		divisor := 1
		for i := 0; i < digits-width; i++ {
			divisor *= 10
		}

		result = (result + power_mod((d/divisor)%mod, d%divisor)) % mod
	}

	return result
}
