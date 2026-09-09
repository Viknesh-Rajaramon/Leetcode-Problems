package main

func minOperations(s1 string, s2 string) int {
	n := len(s1)
	if n == 1 {
		if s1 == "1" && s2 == "0" {
			return -1
		}

		if s1 != s2 {
			return 1
		}

		return 0
	}

	result, l := 0, 0
	for i := range n {
		if s1[i] == '1' && s2[i] == '0' {
			l++
		} else {
			if l > 0 {
				result += (l / 2) + (l%2)*2
				l = 0
			}

			if s1[i] == '0' && s2[i] == '1' {
				result++
			}
		}
	}

	if l > 0 {
		result += (l / 2) + (l%2)*2
	}

	return result
}
