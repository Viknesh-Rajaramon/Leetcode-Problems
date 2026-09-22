package main

import (
	"strconv"
)

func kthDigit(k int64) int {
	if k < 10 {
		return int(k)
	}

	pow := func(x, n int64) int64 {
		if n == 0 {
			return 1
		}

		result := int64(1)
		for n > 0 {
			if n%2 == 1 {
				result *= x
			}

			x *= x
			n /= 2
		}

		return result
	}

	d := int64(1)
	for k > 9*d*pow(10, d-1) {
		k -= 9 * d * pow(10, d-1)
		d++
	}

	b, pos := pow(10, d-2)+((k-1)/(10*d)), (k-1)%(10*d)
	num_idx := pos / d
	if b%2 == 1 {
		num_idx = 9 - num_idx
	}

	return int(strconv.FormatInt(10*b+num_idx, 10)[pos%d] - '0')
}
