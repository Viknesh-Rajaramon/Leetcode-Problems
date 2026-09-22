package main

func elevatorRequests(n int, requests []int) int {
	result, curr := 0, 0
	for _, r := range requests {
		result += max(r-curr, curr-r)
		curr = r
	}

	return result
}
