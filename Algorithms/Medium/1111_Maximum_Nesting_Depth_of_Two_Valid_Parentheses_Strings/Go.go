package main

func maxDepthAfterSplit(seq string) []int {
	result := make([]int, 0)
	for i, c := range seq {
		if c == '(' {
			result = append(result, i%2)
		} else {
			result = append(result, 1-i%2)
		}
	}

	return result
}
