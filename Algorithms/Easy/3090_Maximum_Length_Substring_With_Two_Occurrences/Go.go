package main

func maximumLengthSubstring(s string) int {
	result, l, count := 0, 0, make([]int, 26)
	for r, c := range s {
		ch := c - 'a'
		count[ch]++
		for count[ch] > 2 {
			count[s[l]-'a']--
			l++
		}

		result = max(result, r-l+1)
	}

	return result
}
