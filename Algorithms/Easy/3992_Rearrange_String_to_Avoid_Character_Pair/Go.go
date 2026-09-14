package main

func rearrangeString(s string, x byte, y byte) string {
	result, count_x, count_y := make([]byte, 0), 0, 0
	for i := range s {
		if s[i] == x {
			count_x++
		} else if s[i] == y {
			count_y++
		} else {
			result = append(result, s[i])
		}
	}

	for range count_y {
		result = append(result, y)
	}

	for range count_x {
		result = append(result, x)
	}

	return string(result)
}
