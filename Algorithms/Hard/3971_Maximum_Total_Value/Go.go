package main

func maxTotalValue(value []int, decay []int, m int) int {
	mod, n := int(1e9+7), len(value)
	is_valid := func(x int) bool {
		count := 0
		for i := range n {
			if value[i] >= x {
				count += ((value[i] - x) / decay[i]) + 1
			}
		}

		return count >= m
	}

	low, high := 1, 1
	for _, val := range value {
		high = max(high, val)
	}

	for low <= high {
		mid := (low + high) >> 1
		if is_valid(mid) {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	result, count, threshold := 0, 0, high
	for i := range n {
		if value[i] < threshold {
			continue
		}

		t := (value[i]-threshold)/decay[i] + 1
		count += t
		result = (result + ((t * (2*value[i] - (t-1)*decay[i]) / 2) % mod)) % mod
	}

	result = (result + (threshold * (m - count) % mod)) % mod
	if result < 0 {
		return mod + result
	}

	return result
}
