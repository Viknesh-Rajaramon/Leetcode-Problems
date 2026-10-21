package main

func minOperations(s string) int {
	n, flag, min_c, max_c := len(s), true, s[0], s[0]
	for i := range n - 1 {
		min_c, max_c = min(min_c, s[i+1]), max(max_c, s[i+1])
		if s[i] > s[i+1] {
			flag = false
		}
	}

	if flag {
		return 0
	}

	if n == 2 {
		return -1
	}

	if s[0] == min_c || s[n-1] == max_c {
		return 1
	}

	for i := 1; i < n-1; i++ {
		if s[i] == max_c || s[i] == min_c {
			return 2
		}
	}

	return 3
}
