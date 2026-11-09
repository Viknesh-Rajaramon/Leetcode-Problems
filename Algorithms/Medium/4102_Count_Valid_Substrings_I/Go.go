package main

func countValidSubstrings(s string) int64 {
	result, l := int64(0), 0
	for r := range s {
		if r >= 2 && s[r-2:r+1] == "abc" {
			l = r - 1
		}

		result += int64(r - l + 1)
	}

	return result
}
