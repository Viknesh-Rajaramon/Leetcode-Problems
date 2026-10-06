package main

func minAddToMakeValid(s string) int {
	result, open_count := 0, 0
	for _, c := range s {
		if c == '(' {
			open_count++
		} else {
			if open_count > 0 {
				open_count--
			} else {
				result++
			}
		}
	}

	return result + open_count
}
