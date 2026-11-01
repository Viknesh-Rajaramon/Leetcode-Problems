package main

func minimumMaxValue(n int, index int, value int) int64 {
	get_spf := func(x int) int {
		if x < 2 {
			return 0
		}

		if x%2 == 0 {
			return 2
		}

		if x%3 == 0 {
			return 3
		}

		i := 5
		for i*i <= x {
			if x%i == 0 {
				return i
			}

			if x%(i+2) == 0 {
				return i + 2
			}

			i += 6
		}

		return x
	}

	if value == 1 {
		return int64(-1)
	}

	if index > 0 {
		min_left := 0
		if value%2 == 0 {
			min_left = value - 2*index
		} else {
			spf := get_spf(value)
			if spf == 0 {
				return int64(-1)
			}

			min_left = value - spf - 2*(index-1)
		}

		if min_left <= 0 {
			return int64(-1)
		}
	}

	if index == n-1 {
		return int64(value)
	}

	if value%2 == 0 {
		return int64(value + 2*(n-1-index))
	}

	spf := get_spf(value)
	if spf == 0 {
		return int64(-1)
	}

	return int64(value + spf + 2*(n-2-index))
}
