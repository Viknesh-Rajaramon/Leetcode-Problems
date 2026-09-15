package main

func maxPalindromes(s string, k int) int {
	check := func(l, r int) bool {
		for l < r {
			if s[l] != s[r] {
				return false
			}

			l++
			r--
		}

		return true
	}

	result, n, start := 0, len(s), 0
	for r := k - 1; r < n; r++ {
		l := r - k + 1
		if l >= start && check(l, r) {
			result++
			start = r + 1
			continue
		}

		l = r - k
		if l >= start && check(l, r) {
			result++
			start = r + 1
		}
	}

	return result
}
