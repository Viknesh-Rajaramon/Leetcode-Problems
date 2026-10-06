package main

func minRotations(s string) int {
	result, curr := 0, 0
	for _, c := range s {
		d := int(c - '0')
		result += min((d-curr+10)%10, (curr-d+10)%10)
		curr = d
	}

	return result
}
