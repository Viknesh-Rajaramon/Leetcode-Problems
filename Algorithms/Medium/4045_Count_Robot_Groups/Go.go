package main

func countGroups(position []int, speed []int, distance int) int {
	n := len(position)
	result, right := n, n-1
	for i := n - 2; i >= 0; i-- {
		if position[i+1]-position[i] <= distance || speed[i] > speed[right] {
			result--
		} else {
			right = i
		}
	}

	return result
}
