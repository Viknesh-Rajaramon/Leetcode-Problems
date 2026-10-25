package main

func countMagicalPairs(s string) int {
	result, n := 0, len(s)
	for j := range n - 1 {
		r, hs := make([]int, 27), make(map[byte]bool)
		for k := j + 1; k < n; k++ {
			hs[s[k]] = true
			r[len(hs)]++
		}

		clear(hs)
		for i := j; i >= 0; i-- {
			hs[s[i]] = true
			result += r[len(hs)]
		}
	}

	return result
}
