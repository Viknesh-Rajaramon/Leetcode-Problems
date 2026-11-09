package main

func countValidSubstrings(s string) int64 {
	result, a, ab, abc := int64(0), -1, -1, -1
	for i, c := range s {
		if c == 'a' {
			a = i
		} else if c == 'b' && a != -1 {
			ab = a
		} else if c == 'c' && ab != -1 {
			abc = ab
		}

		result += int64(i - abc)
	}

	return result
}
