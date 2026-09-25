package main

func isPalindromic(s string) bool {
	l, r := 0, len(s)-1
	for l <= r {
		for bit := 7; bit >= 0; bit-- {
			left, right := (s[l]>>bit)&1, (s[r]>>(7-bit))&1
			if left != right {
				return false
			}
		}

		l++
		r--
	}

	return true
}
