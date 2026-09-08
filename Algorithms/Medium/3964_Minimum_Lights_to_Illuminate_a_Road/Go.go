package main

func minLights(lights []int) int {
	n := len(lights)
	diff := make([]int, n+1)
	for i, v := range lights {
		if v == 0 {
			continue
		}

		diff[max(0, i-v)]++
		diff[min(n-1, i+v)+1]--
	}

	for i := range n {
		diff[i+1] += diff[i]
	}

	result, length := 0, 0
	for i := range n {
		if diff[i] == 0 {
			length++
		} else {
			result += (length + 2) / 3
			length = 0
		}
	}

	result += (length + 2) / 3
	return result
}
