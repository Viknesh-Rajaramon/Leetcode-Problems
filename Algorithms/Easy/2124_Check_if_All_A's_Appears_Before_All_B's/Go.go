package main

func checkString(s string) bool {
	seen_b := false
	for _, c := range s {
		if c == 'a' && seen_b {
			return false
		} else if c == 'b' {
			seen_b = true
		}
	}

	return true
}
